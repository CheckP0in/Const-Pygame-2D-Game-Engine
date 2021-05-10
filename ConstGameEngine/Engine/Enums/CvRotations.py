# -- import dependencies -- #
from enum import Enum
from cv2.cv2 import ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE, ROTATE_180


# -- Create class -- #
class CvRotations(Enum):
    CLOCK_90 = ROTATE_90_CLOCKWISE  # -- Used for rotating an image 90 degrees clockwise -- #
    COUNTER_CLOCK_90 = ROTATE_90_COUNTERCLOCKWISE  # -- Used for rotating an image 90 degrees counter clockwise -- #
    ROTATE_180 = ROTATE_180  # -- Used for rotating an image 180 degrees -- #
