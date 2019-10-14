# Discord Post Generator
Fake posts created using Markov chains from existing Discord posts. Discord is a chat app which allows users to invite their friends to servers. Servers are split into channels, used to separate discussions by topic. This program reads Discord chat logs from CSV files contained in folders - a folder represents a server, a CSV file represents one whole channel, and each row in a CSV file contains data about one message posted in that channel.

Running this program, the user is first asked to select a directory (representing a Discord server) to work with, if there are multiple. Then, they are asked to provide a Discord tag (a username, in the format MyName#1234), a length for generated posts, and the number of posts to be generated. The program then gets all posts made by that user from all channels found in the selected directory, and constructs a Markov chain to create new posts with. These are usually nonsense, but are fairly amusing. The user can also choose to use all posts from all channels in a server to construct new posts, rather than just the posts of a single user.

# User Guide
Discord channels can be exported as CSV files for use with this program using [DiscordChatExporter by Tyrrrz](https://github.com/Tyrrrz/DiscordChatExporter). For ethical reasons, no logs are included with this repository. When exporting logs yourself, make sure you select CSV as the file format to export to (rather than HTML or TXT). Exported CSV files should be placed in a folder, and that folder should be placed in the same directory as the main program file. Once you have your chat logs ready, you can run the program. Python 3 must be installed.

# v1.0 Changelog
 - Added discord_post_generator.py!
 
 # What Did I Learn?
  - All about Markov chains!
  - Practice navigating file structures and parsing CSV files.
