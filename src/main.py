import glob
import pathlib

import cv2
import torch
import torchvision

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Find all the images of left-handed writing
left_hand_images = [cv2.imread(file) for file in glob.glob(
    './img/left/*') if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]

# Find all images of right-handed writing
right_hand_images = [cv2.imread(file) for file in glob.glob(
    './img/right/*') if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]