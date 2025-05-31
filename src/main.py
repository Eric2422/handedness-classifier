import glob

import cv2
import torch
import torchvision

left_hand = [cv2.imread(file) for file in glob.glob("img/left/*.jpg")]
print(left_hand)

right_hand = [cv2.imread(file) for file in glob.glob("img/right/*.jpg")]
print(right_hand)