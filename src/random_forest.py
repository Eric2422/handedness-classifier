from os import listdir
from pathlib import Path

from natsort import natsorted
import skimage as ski
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


IMG_DIRECTORY = Path('./img')
LEFT_DIRECTORY = IMG_DIRECTORY / 'left'
RIGHT_DIRECTORY = IMG_DIRECTORY / 'right'

# List of accepted image file extensions
ACCEPTED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Get all the images of left-handed writing
left_files = [file for file in natsorted(listdir(
    LEFT_DIRECTORY)) if Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
left_images = [ski.io.imread(LEFT_DIRECTORY / file) for file in left_files]

# Get all images of right-handed writing
right_files = [file for file in natsorted(listdir(
    RIGHT_DIRECTORY)) if Path(file).suffix.lower() in ACCEPTED_EXTENSIONS]
right_images = [ski.io.imread(RIGHT_DIRECTORY / file) for file in right_files]

# Combine the data into a single array
x_data = [img for img in left_images + right_images]
y_data = [0] * len(left_images) + [1] * len(right_images)

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2
)

clf = RandomForestClassifier()
clf = clf.fit(x_train, y_train)

# Check the accuracy of the model
accuracy = clf.score(x_test, y_test)
print(f'Accuracy: {accuracy}')