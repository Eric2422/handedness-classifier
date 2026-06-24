# ambidexterity-test

A small computer vision program to try and distinguish left- and right-handed handwriting.

## [Cache](./cache/)

Stores previously trained models.

## [Reddit Scraper]

The [Reddit scraper] gathers images off [Reddit] to help train the model.
See below for more details.

[Reddit scraper]: ./src/reddit_scraper.py
[Reddit]: https://www.reddit.com

### [`praw.ini`]

When you clone this repo, copy the contents of [`praw.ini.sample`](./praw.ini.sample)
into a new file at [`./praw.ini`] to configure the Reddit crawler.
Then fill in the empty fields with the necessary information.

[`./praw.ini`]: ./praw.ini

### [`search/`]

The [`search/`] directory contains CSV files.
The first row stores subreddits to search through,
and the second row stores keywords to use for the search.

[`search/`]: ./search/

### [`img/scraper`]

The [`img/scraper`] directory stores the images that the Reddit scraper finds.

The Reddit scraper will create a new directory for each subreddit it searches through.
Additionally, each subreddit will have a subdirectory for each keyword searched.
Each image will be stored under the subreddit it came from
and the keyword that found it.

The scraper will produce a file named `search-results.json` with more information
about the Reddit post that the image was extracted from.

[`img/scraper`]: ./img/scraper
