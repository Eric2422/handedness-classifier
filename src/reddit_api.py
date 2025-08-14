import configparser
import csv
import sys
import pathlib

import http.client
import io
import PIL.Image
import praw
import requests


def read_image_from_url(url: str) -> PIL.Image.Image:
    """Read an image from a URL.

    Parameters
    ----------
    url : str
        A string uniform resource locator(URL) to read the image from.

    Returns
    -------
    PIL.Image.Image
        The image stored at the URL, stored as a Python Image Library(PIL) image.

    Raises
    ------
    ConnectionError
        The image could not be read from the URL.
    """
    request = requests.get(url)

    # Read image
    try:
        return PIL.Image.open(io.BytesIO(request.content))

    # Most failures seem to be from imgur, with an error of "429: Too Many Requests"
    except PIL.UnidentifiedImageError:
        raise ConnectionError(
            f'Image failed to open: {url} \nError {request.status_code}: {http.client.responses[request.status_code]}')


SUBREDDITS = tuple()
"""List of subreddits to search through."""
KEYWORDS = tuple()
"""List of key words to search with."""

IMAGE_FORMATS = ('jpg', 'jpeg', 'png')
"""List of image file extensions that will be saved."""
IMAGE_DIRECTORY = pathlib.Path('img')
"""The directory that all images are saved to."""

try:
    file_name = sys.argv[1]
    with open(file_name) as csv_file:
        csv = csv.reader(csv_file)

        SUBREDDITS = [entry.strip() for entry in csv.__next__()]
        KEYWORDS = [entry.strip().lower() for entry in csv.__next__()]

except IndexError:
    print('You need to pass in the name of the file containing the subreddits and search keywords.')

# Retrieve the subreddits and keywords to search for
config = configparser.ConfigParser()
config.read('./praw.ini')

# Log into reddit
reddit = praw.Reddit(
    client_id=config['DEFAULT']['client_id'],
    client_secret=config['DEFAULT']['client_secret'],
    password=config['DEFAULT']['password'],
    user_agent=config['DEFAULT']['user_agent'],
    username=config['DEFAULT']['username'],
)

# Search each given subreddit
for subreddit_name in SUBREDDITS:
    subreddit = reddit.subreddit(subreddit_name)
    print(f'----{subreddit.display_name.upper()}-----\n\n')

    # Search for each given keyword
    for keyword in KEYWORDS:
        print(f'---{keyword.title()}---')
        for search_result in subreddit.search(keyword):
            url = search_result.url

            # Filter search results for images
            if url.endswith(IMAGE_FORMATS):
                try:
                    image = read_image_from_url(url)
                    image.save(IMAGE_DIRECTORY / keyword.replace(' ', '_') /
                               pathlib.Path(url).name)
                    print()

                except Exception as err:
                    print(err)

        print()

    print()

print()
