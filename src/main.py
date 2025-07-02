import os
import pathlib

import cv2
import natsort
import skimage as ski

IMG_DIRECTORY = pathlib.Path('./img')
LEFT_DIRECTORY = IMG_DIRECTORY / 'left'
RIGHT_DIRECTORY = IMG_DIRECTORY / 'right'

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Get all the images of left-handed writing
left_files = [file for file in natsort.natsorted(os.listdir(
    LEFT_DIRECTORY)) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]

left_images = [ski.io.imread(LEFT_DIRECTORY / file) for file in left_files]
print(left_images)

# Get all images of right-handed writing
right_files = [file for file in natsort.natsorted(os.listdir(
    RIGHT_DIRECTORY)) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
print(right_files)

right_images = [ski.io.imread(RIGHT_DIRECTORY / file) for file in right_files]
print(right_images)