import os
import pathlib
import sys

import joblib
import numpy as np
import numpy.typing as npt
import skimage as ski
import sklearn.ensemble
import sklearn.model_selection


def read_image_directory(directory_path: str | pathlib.Path) -> npt.NDArray:
    """Read a directory of images and return its contents.

    Any images with file endings included in `IMAGE_FILE_EXTENSIONS` are accepted.

    Parameters
    ----------
    directory_path : str | pathlib.Path
        A string or `Path` object that points to a directory of images.

    Returns
    -------
    npt.NDArray
        The contents of the directory represented as a multi-dimensional NumPy array.
    """
    # Retrieve all the filepaths within the directory
    filepaths = [
        file for file in os.listdir(directory_path)
        if pathlib.Path(file).suffix.lower() in IMAGE_FILE_EXTENSIONS
    ]

    # For each filepath, read the file.
    images = [
        (
            # If the filepath points to a PNG file, strip the PNG of its alpha value.
            ski.io.imread(LEFT_DIRECTORY / file)[:, :, :-1] if file.endswith('.png')
            else ski.io.imread(LEFT_DIRECTORY / file)
        )
        for file in filepaths
    ]

    return np.array(images)


IMAGE_DIRECTORY = pathlib.Path('./img')
"""The directory that stores images of handwriting."""
LEFT_DIRECTORY = IMAGE_DIRECTORY / 'left'
"""The directory that stores images of left-handed writing."""
RIGHT_DIRECTORY = IMAGE_DIRECTORY / 'right'
"""The directory that stores images of right-handed writing."""

IMAGE_FILE_EXTENSIONS = ('.jpg', '.jpeg', '.png')
"""List of accepted image file extensions."""

MODEL_DIRECTORY = pathlib.Path('./cache')
memory = joblib.Memory(MODEL_DIRECTORY)

VALIDATION_PROPORTION: float
"""
    The proportion of total data that will be used for validation,
    e.g., if the value is `0.2`, 20% of the data will be used for validation.
"""

TEST_DATA_PROPORTION: float
"""
    The proportion of total data that will be used for testing,
    e.g., if the value is `0.2`, 20% of the data will be used for testing.
"""

try:
    VALIDATION_PROPORTION = float(sys.argv[1])
    TEST_DATA_PROPORTION = float(sys.argv[2])

except:
    VALIDATION_PROPORTION = 0.1
    TEST_DATA_PROPORTION = 0.2

# Get all the images of left-handed writing
left_images = read_image_directory(LEFT_DIRECTORY)

# Get all images of right-handed writing
right_images = read_image_directory(LEFT_DIRECTORY)

# Combine the data into a single array
x_data = [img for img in left_images + right_images]
y_data = [0] * len(left_images) + [1] * len(right_images)

# Split the data into training and testing data.
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x_data, y_data, test_size=TEST_DATA_PROPORTION
)

clf = sklearn.ensemble.RandomForestClassifier()

# Cache the tree to avoid having to retrain the it each time the program runs.
memory.cache(clf.fit)
clf = clf.fit(x_train, y_train)

# Check the accuracy of the model
accuracy = clf.score(x_test, y_test)
print(f'Accuracy: {accuracy}')
