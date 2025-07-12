import configparser
import time

import praw
import pathlib


CONFIG = configparser.ConfigParser()
CONFIG.read('./praw.ini')

REDDIT = praw.Reddit(
    client_id=CONFIG['DEFAULT']['client_id'],
    client_secret=CONFIG['DEFAULT']['client_secret'],
    password=CONFIG['DEFAULT']['password'],
    user_agent=CONFIG['DEFAULT']['user_agent'],
    username=CONFIG['DEFAULT']['username'],
)

print(REDDIT.user.me())