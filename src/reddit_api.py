import configparser
import csv
import sys
import time

import praw

try:
    file_name = sys.argv[1]
    with open(file_name) as csv_file:
        csv = csv.reader(csv_file)

        SUBREDDITS = csv.__next__()
        """List of subreddits to search through."""

        KEYWORDS = csv.__next__()
        """List of key words to search with."""


except IndexError:
    print('You need to pass in the name of the file containg the subreddits and search keywords.')

CONFIG = configparser.ConfigParser()
CONFIG.read('./praw.ini')

REDDIT = praw.Reddit(
    client_id=CONFIG['DEFAULT']['client_id'],
    client_secret=CONFIG['DEFAULT']['client_secret'],
    password=CONFIG['DEFAULT']['password'],
    user_agent=CONFIG['DEFAULT']['user_agent'],
    username=CONFIG['DEFAULT']['username'],
)

(REDDIT.subreddit(subreddit).search() for subreddit in SUBREDDITS)
for subreddit_name in SUBREDDITS:
    subreddit = REDDIT.subreddit(subreddit_name)
    print(f'\n\n\n-----{subreddit.display_name.upper()}-----', end='\n\n\n')

    for keyword in KEYWORDS:
        print(f'---{keyword.title()}---')
        for search_result in subreddit.search(keyword):
            print(f'\t{search_result.title}')

        print()

    print(end='\n\n')
