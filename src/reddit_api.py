import configparser
import csv
import sys

import praw

SUBREDDITS = []
KEYWORDS = []

try:
    file_name = sys.argv[1]
    with open(file_name) as csv_file:
        csv = csv.reader(csv_file)

        SUBREDDITS = csv.__next__()
        """List of subreddits to search through."""

        KEYWORDS = csv.__next__()
        """List of key words to search with."""


except IndexError:
    print('You need to pass in the name of the file containing the subreddits and search keywords.')

CONFIG = configparser.ConfigParser()
CONFIG.read('./praw.ini')

reddit = praw.Reddit(
    client_id=CONFIG['DEFAULT']['client_id'],
    client_secret=CONFIG['DEFAULT']['client_secret'],
    password=CONFIG['DEFAULT']['password'],
    user_agent=CONFIG['DEFAULT']['user_agent'],
    username=CONFIG['DEFAULT']['username'],
)

# search_results = [[reddit.subreddit(subreddit).search(keyword) for keyword in KEYWORDS] for subreddit in SUBREDDITS]
# print(search_results)

for subreddit_name in SUBREDDITS:
    subreddit = reddit.subreddit(subreddit_name)
    print(f'\n\n\n-----{subreddit.display_name.upper()}-----', end='\n\n\n')

    for keyword in KEYWORDS:
        print(f'---{keyword.title()}---')
        for search_result in subreddit.search(keyword):
            print(f'\t{search_result.title}')
            
            print(f'{search_result.url}')

        print()

    print(end='\n\n')
