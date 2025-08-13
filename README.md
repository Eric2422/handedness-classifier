# ambidexterity-test

A small computer vision program to try and distinguish left- and right-handed handwriting.

## `praw.ini`

When you clone this repo, copy the contents of [`praw.ini.sample`](./praw.ini.sample)
into a new file called `./praw.ini` to configure the Reddit crawler.
Then fill in the empty fields with the necessary information.

## `search/`

The [`search/`](.search) directory contains CSV files.
The first row stores subreddits to search through, and the second row stores keywords to use for the search.
