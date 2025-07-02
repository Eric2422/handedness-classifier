import os
import pathlib

import cv2
import natsort
import skimage as ski

IMG_DIRECTORY = './img'

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Get all the images of left-handed writing
left_files = [file for file in natsort.natsorted(os.listdir(
    f'{IMG_DIRECTORY}/left')) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
print(left_files)

left_images = [ski.io.imread(f'{IMG_DIRECTORY}/left/{file}') for file in left_files]

# Get all images of right-handed writing
right_files = [file for file in natsort.natsorted(os.listdir(
    f'{IMG_DIRECTORY}/right')) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
print(right_files)

right_images = [ski.io.imread(f'{IMG_DIRECTORY}/right/{file}') for file in right_files]
