import configparser
import csv
import sys

import  http.client
import io
import PIL.Image
import praw
import requests

SUBREDDITS = tuple()
"""List of subreddits to search through."""
KEYWORDS = tuple()
"""List of key words to search with."""
IMAGE_FORMATS = ('jpg', 'jpeg', 'png')
"""List of image file extensions that will be saved."""

try:
    file_name = sys.argv[1]
    with open(file_name) as csv_file:
        csv = csv.reader(csv_file)

        SUBREDDITS = csv.__next__()
        KEYWORDS = csv.__next__()

except IndexError:
    print('You need to pass in the name of the file containing the subreddits and search keywords.')

config = configparser.ConfigParser()
config.read('./praw.ini')

reddit = praw.Reddit(
    client_id=config['DEFAULT']['client_id'],
    client_secret=config['DEFAULT']['client_secret'],
    password=config['DEFAULT']['password'],
    user_agent=config['DEFAULT']['user_agent'],
    username=config['DEFAULT']['username'],
)

for subreddit_name in SUBREDDITS:
    subreddit = reddit.subreddit(subreddit_name)
    print(f'----{subreddit.display_name.upper()}-----\n\n')

    for keyword in KEYWORDS:
        print(f'---{keyword.title()}---')
        for search_result in subreddit.search(keyword):

            url = search_result.url
            if url.endswith(IMAGE_FORMATS):
                request = requests.get(url)

                try:
                    image = PIL.Image.open(io.BytesIO(request.content))

                except PIL.UnidentifiedImageError:
                    print(f'Image failed to open: {url}')
                    print(f'Err {request.status_code}: {http.client.responses[request.status_code]}')

        print()

    print()

print()