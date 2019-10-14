import numpy as np
import csv, os, random
from collections import defaultdict

# convert non-supported characters (like emojis) into placeholder
def bmp(s):
    return "".join(i if ord(i) < 10000 else '\ufffd' for i in s)

# generate a post recursively
def walk(m, d=12, s=None):
    if d <= 0:
        return []

    if s == None:
        s = random.choice(list(m.keys()))
  
    weights = np.array(list(m[s].values()), dtype=np.float64)
    weights /= weights.sum()

    choices = list(m[s].keys())
    choice = np.random.choice(choices, None, p=weights)
  
    return [choice] + walk(m, d=d-1, s=choice)

# generate and return a list of posts, given a directory, discord tag, post length and post count
def get_posts(d, t, l, c):
    word_list = []

    # produce a list of words from the user's posts (or all posts, if selected)
    for file in os.listdir(d):
        with open(f'{d}/{file}', encoding='utf8') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if (t.lower() != d.lower() and row[1].lower() == t.lower()) or (t.lower() == d.lower() and row[1] != "Author"):
                    for word in row[3].split(' '):
                        word_list.append(bmp(word).lower())

    # return an empty list is there are no posts associated with the given tag
    if word_list == []:
        return []

    # construct the markov chain
    markov = defaultdict(lambda: defaultdict(int))
    for prev, curr in zip(word_list[:-1], word_list[1:]):
        markov[prev][curr] += 1

    # construct and return a list of length c of posts of length l using the markov chain
    posts = []
    for i in range(c):
        posts.append(' '.join(walk(markov, d=l)))

    return posts

# get directory and tag input, then generate posts based on user's existing ones
def run():
    dirs = []
    dir_string = ""
    for (i, d) in zip(range(len(os.listdir())), os.listdir()):
        if os.path.isdir(d):
            dirs.append((i, d))
            dir_string += f"{i}. {d}\n"

    # get directory input, unless there is only one directory
    if len(dirs) > 1:
        directory = input(f"What directory would you like to use channels from? Enter a number:\n{dir_string}> ")
    else:
        directory = dirs[0][0]
    
    for (i, d) in dirs:
        if int(directory) == i:
            directory = d
            break
    
    tag = input(f"\nWho would you like to speak to? Enter a Discord tag, or \"{directory}\" to use all messages:\n> ")
    length = int(input(f"\nEnter the length of each post to be generated:\n> "))
    count = int(input(f"\nEnter the number of posts to be generated:\n> "))
    
    posts = get_posts(directory, tag, length, count)
    print(f"\n{tag} has this to say...\n")
    for p in posts:
        print(p, '\n')

    print("-----\n")

while True:
    run()
