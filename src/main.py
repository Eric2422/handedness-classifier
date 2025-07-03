import os
import pathlib

import natsort
import numpy as np
import skimage as ski
import sklearn.tree

IMG_DIRECTORY = pathlib.Path('./img')
LEFT_DIRECTORY = IMG_DIRECTORY / 'left'
RIGHT_DIRECTORY = IMG_DIRECTORY / 'right'

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Get all the images of left-handed writing
left_files = [file for file in natsort.natsorted(os.listdir(
    LEFT_DIRECTORY)) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]

left_images = [ski.io.imread(LEFT_DIRECTORY / file) for file in left_files]
# print(left_images)

# Get all images of right-handed writing
right_files = [file for file in natsort.natsorted(os.listdir(
    RIGHT_DIRECTORY)) if pathlib.Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]

right_images = [ski.io.imread(RIGHT_DIRECTORY / file) for file in right_files]
# print(right_images)

x_data = [img for img in left_images + right_images]
print(x_data)

y_data = [0] * len(left_images) + [1] * len(right_images)

clf = sklearn.tree.DecisionTreeClassifier()
clf = clf.fit(x_data, y_data)
