# ambidexterity-test

A small computer vision program to try and distinguish left- and right-handed handwriting.

## [Random Forest](./src/random_forest.py)

[`random_forest.py`](./src/random_forest.py) trains a random forest model
based on the images in [`img/left_hand`](./img/left_hand/) and [`img/right_hand`](./img/right_hand/).
Then, the model attempts to classify the images in [`img/input`](./img/input/) into left hand or right hand.

The program will default to splitting the data into training, validation and test with a ratio of 70:10:20.
If you wish to use a different proportion of the data for testing, pass it in as a command-line arguments:
`python src/random_forest.py <validation data proportion> <test data proportion>`,
e.g., `python src/random_forest.py 0.15 0.25`.

Caches the result into the [`cache/`](./cache/) directory.

### [Cache](./cache/)

Stores previously trained models.

## [Reddit Scraper](./src/reddit_scraper.py)

The [Reddit scraper](./src/reddit_scraper.py) helps you gather images to train the models.
See below for more details.

### `praw.ini`

When you clone this repo, copy the contents of [`praw.ini.sample`](./praw.ini.sample)
into a new file at `./praw.ini` to configure the Reddit crawler.
Then fill in the empty fields with the necessary information.

### [`search/`](./search/)

The [`search/`](.search) directory contains CSV files.
The first row stores subreddits to search through, and the second row stores keywords to use for the search.

### [`img/scraper`](./img/scraper)

The [`img/scraper`](./img/scraper) directory stores the images that the Reddit scraper finds.

The Reddit scraper will create a new directory for each subreddit it searches through.
Additionally, each subreddit will have a subdirectory for each keyword searched.
Each image will be stored under the subreddit it came from and the keyword that found it.

The scraper will produce a file named `search-results.json` with more information
about the Reddit post that the image was extracted from.
