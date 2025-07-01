import os
import pathlib

import cv2
import natsort
import skimage as ski

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Get all the images of left-handed writing
left_hand_files = [file for file in natsort.natsorted(os.listdir(
    './img/left')) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
print(left_hand_files)

# Get all images of right-handed writing
right_hand_files = [file for file in natsort.natsorted(os.listdir(
    './img/right')) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
print(right_hand_files)