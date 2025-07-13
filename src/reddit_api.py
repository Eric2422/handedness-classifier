import configparser
import time

import praw


CONFIG = configparser.ConfigParser()
CONFIG.read('./praw.ini')

REDDIT = praw.Reddit(
    client_id=CONFIG['DEFAULT']['client_id'],
    client_secret=CONFIG['DEFAULT']['client_secret'],
    password=CONFIG['DEFAULT']['password'],
    user_agent=CONFIG['DEFAULT']['user_agent'],
    username=CONFIG['DEFAULT']['username'],
)

SUBREDDITS = ("handwriting",)
"""List of subreddits to search through."""

KEY_WORDS = ('ambidextrous', 'left hand', 'right hand')
"""List of key words to search with."""

(REDDIT.subreddit(subreddit).search() for subreddit in SUBREDDITS)
for subreddit_name in SUBREDDITS:
    subreddit = REDDIT.subreddit(subreddit_name)
    print(f'\n\n\n-----{subreddit.display_name.upper()}-----', end='\n\n\n')

    for key_word in KEY_WORDS:
        print(f'---{key_word.title()}---')
        for search_result in subreddit.search(key_word):
            print(f'\t{search_result.title}')

        print()

    print(end='\n\n')
