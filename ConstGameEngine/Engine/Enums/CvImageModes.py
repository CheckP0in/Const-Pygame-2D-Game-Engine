from enum import Enum

import cv2


class CvImageModes(Enum):
    COLOUR = cv2.IMREAD_COLOR  # RGB values without alpha values
    GRAYSCALE = cv2.IMREAD_GRAYSCALE  # Grayscale image without alpha values
    UNCHANGED = cv2.IMREAD_UNCHANGED  # RGB values with alpha values
