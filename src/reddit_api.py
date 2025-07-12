import time

import praw
import pathlib

CONFIG_FILE = pathlib.Path('./praw.ini')

reddit = praw.Reddit(
    site_name='bot',
    
)
