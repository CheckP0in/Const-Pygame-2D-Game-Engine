# -- Import Dependencies -- #
import cv2
import os


# -- Create class -- #
class Image:
    # -- Loads an image and returns a cv2 image object -- #
    @staticmethod
    def load(image_dir: str, mode):
        return cv2.imread(image_dir, mode)

    # -- Resizes the image given to a new size or scale -- #
    @staticmethod
    def resize(img: cv2.imread, width: int, height: int, width_multiplier=1.0, height_multiplier=1.0):
        if (width_multiplier < 1.0 or width_multiplier > 1.0) and (height_multiplier < 1.0 or height_multiplier > 1.0):
            return cv2.resize(img, (0, 0), fx=width_multiplier, fy=height_multiplier)

        else:
            return cv2.resize(img, (width, height))

    # -- rotates the given image to the new rotation -- #
    @staticmethod
    def rotate(img, rotation):
        return cv2.rotate(img, rotation)

    # -- Saves the given image to the given directory. If the image already exists in the given directory, the image is replaced -- #
    @staticmethod
    def save(image_dir, img):
        temp_dir = image_dir.split('/')
        if os.path.exists(final_dir := os.path.join(temp_dir[0], '/'.join(temp_dir[1:]))):
            os.remove(final_dir)
            cv2.imwrite(final_dir, img)

        else:
            cv2.imwrite(final_dir, img)
