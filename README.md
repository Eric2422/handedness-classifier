# ambidexterity-test

A small computer vision program to try and distinguish left- and right-handed handwriting.

## Random Forest

[`random_forest.py`](./src/random_forest.py) trains a random forest model based on the images in [`img/left_hand`](./img/left_hand/) and [`img/right_hand`](./img/right_hand/).
Caches the result into the [`cache/`](./cache/) directory.

### Cache

Stores previously trained models.

## Reddit Scraper

The [Reddit scraper](./src/reddit_scraper.py) helps you gather images to train the models.
See below for more details.

### `praw.ini`

When you clone this repo, copy the contents of [`praw.ini.sample`](./praw.ini.sample)
into a new file at `./praw.ini` to configure the Reddit crawler.
Then fill in the empty fields with the necessary information.

### `search/`

The [`search/`](.search) directory contains CSV files.
The first row stores subreddits to search through, and the second row stores keywords to use for the search.
