import os
import pathlib

import numpy as np
import numpy.typing as npt
import skimage as ski

IMAGE_DIRECTORY = pathlib.Path('./images')
"""The directory that stores images of handwriting."""
INPUT_DIRECTORY = IMAGE_DIRECTORY / 'input'
"""Stores the images that will be classified based on the trained model."""
TRAINING_DIRECTORY = IMAGE_DIRECTORY / 'training'
"""Stores the images used for training."""
LEFT_DIRECTORY = TRAINING_DIRECTORY / 'left'
"""The directory that stores images of left-handed writing."""
RIGHT_DIRECTORY = TRAINING_DIRECTORY / 'right'
"""The directory that stores images of right-handed writing."""

IMAGE_FILE_EXTENSIONS = ('.jpg', '.jpeg', '.png')
"""List of accepted image file extensions."""

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

    directory = pathlib.Path(directory_path)

    # For each filepath, read the file.
    images = [
        (
            # If the filepath points to a PNG file, strip the PNG of its alpha value.
            ski.io.imread(directory / file)[:, :, :-1] if file.endswith('.png')
            else ski.io.imread(directory / file)
        )
        for file in filepaths
    ]

    return np.array(images)
