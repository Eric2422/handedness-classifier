import configparser
import csv
import sys
import pathlib

import http.client
import io
import json
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


def search_subreddit_for_keyword(subreddit, keyword):
    keyword_dict: dict[str, dict[str, str]] = dict()

    # If there is not a directory in `subreddit_directory` for the keyword,
    # create it.
    keyword_directory = subreddit_directory / keyword
    if not keyword_directory.is_dir():
        keyword_directory.mkdir()

    for search_result in subreddit.search(keyword):
        url = search_result.url

        # Filter search results for images.
        if url.endswith(IMAGE_FORMATS):
            try:
                image = read_image_from_url(url)

                # Save the image.
                filepath = keyword_directory / pathlib.Path(url).name
                image.save(
                    filepath
                )

                keyword_dict[filepath.as_posix()] = {
                    'title': search_result.title,
                    'url': url
                }
                print(f'Image successfully downloaded: {url}')

            except Exception as err:
                print()
                print(err)
                print()

    return keyword_dict


IMAGE_FORMATS = ('jpg', 'jpeg', 'png')
"""The list of image file extensions that will be saved."""
SCRAPER_DIRECTORY = pathlib.Path('./img/scraper')
"""The directory that all images are saved to."""

subreddits: list[str] = list()
"""The list of subreddits to search through."""
keywords: list[str] = list()
"""The list of keywords to search for."""

try:
    # Open the input file provided by the user.
    file_name = sys.argv[1]
    with open(file_name) as csv_file:
        csv = csv.reader(csv_file)

        # Save the subreddits to search through.
        for entry in csv.__next__():
            subreddits.append(entry.strip())

        # Save the keywords to search for.
        for entry in csv.__next__():
            keywords.append(entry.strip().lower())

except IndexError:
    print('You need to pass in the name of the file containing the subreddits and search keywords.')

# Retrieve the subreddits and keywords to search for.
config = configparser.ConfigParser()
config.read('./praw.ini')

# Log into reddit.
reddit = praw.Reddit(
    client_id=config['DEFAULT']['client_id'],
    client_secret=config['DEFAULT']['client_secret'],
    password=config['DEFAULT']['password'],
    user_agent=config['DEFAULT']['user_agent'],
    username=config['DEFAULT']['username'],
)

search_results: dict[str, dict[str, dict[str, str]]] = dict()

# Search each given subreddit.
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    print(f'-----r/{subreddit.display_name}-----\n\n')

    # If there is not a directory in `SCRAPER_DIRECTORY` for the subreddit,
    # create it.
    subreddit_directory = SCRAPER_DIRECTORY / str(subreddit)
    if not subreddit_directory.is_dir():
        subreddit_directory.mkdir()

    subreddit_dict = dict()

    # Search for each given keyword.
    for keyword in keywords:
        print(f'---Searching for "{keyword}"---')

        subreddit_dict[keyword] = search_subreddit_for_keyword(subreddit, keyword)
        print()

    search_results[subreddit_name] = subreddit_dict

with open('img/scraper/search-results.json', 'w', encoding='utf-8') as file:
    json.dump(search_results, file, ensure_ascii=False, indent=4)
