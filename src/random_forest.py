import pathlib
import sys

import joblib
import sklearn.ensemble
import sklearn.model_selection

import image_reader

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
left_images = image_reader.read_image_directory(image_reader.LEFT_DIRECTORY)

# Get all images of right-handed writing
right_images = image_reader.read_image_directory(image_reader.RIGHT_DIRECTORY)

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
