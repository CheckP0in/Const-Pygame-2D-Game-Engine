# -- Import Dependencies -- #
import cv2
import os
from numba import jit, njit


# -- Create class -- #
class Image:
    # -- Loads an image and returns a cv2 image object -- #
    @staticmethod
    def load(image_dir: str, mode):
        return cv2.imread(image_dir, mode)

    @jit(nopython=False)
    def load_jit(self, image_dir: str, mode):
        return cv2.imread(image_dir, mode)

    @njit
    def load_njit(self, image_dir: str, mode):
        return cv2.imread(image_dir, mode)

    # -- Resizes the image given to a new size or scale -- #
    @staticmethod
    def resize(img: cv2.imread, width: int, height: int, width_multiplier=1.0, height_multiplier=1.0):
        if (width_multiplier < 1.0 or width_multiplier > 1.0) and (height_multiplier < 1.0 or height_multiplier > 1.0):
            return cv2.resize(img, (0, 0), fx=width_multiplier, fy=height_multiplier)

        else:
            return cv2.resize(img, (width, height))

    @jit(nopython=False)
    def resize_jit(self, img: cv2.imread, width: int, height: int, width_multiplier=1.0, height_multiplier=1.0):
        if (width_multiplier < 1.0 or width_multiplier > 1.0) and (height_multiplier < 1.0 or height_multiplier > 1.0):
            return cv2.resize(img, (0, 0), fx=width_multiplier, fy=height_multiplier)

        else:
            return cv2.resize(img, (width, height))

    @njit
    def resize_njit(self, img: cv2.imread, width: int, height: int, width_multiplier=1.0, height_multiplier=1.0):
        if (width_multiplier < 1.0 or width_multiplier > 1.0) and (height_multiplier < 1.0 or height_multiplier > 1.0):
            return cv2.resize(img, (0, 0), fx=width_multiplier, fy=height_multiplier)

        else:
            return cv2.resize(img, (width, height))

    # -- rotates the given image to the new rotation -- #
    @staticmethod
    def rotate(img, rotation):
        return cv2.rotate(img, rotation)

    @jit(nopython=False)
    def rotate_jit(self, img, rotation):
        return cv2.rotate(img, rotation)

    @njit
    def rotate_njit(self, img, rotation):
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

    @jit(nopython=False)
    def save_jit(self, image_dir, img):
        temp_dir = image_dir.split('/')
        if os.path.exists(final_dir := os.path.join(temp_dir[0], '/'.join(temp_dir[1:]))):
            os.remove(final_dir)
            cv2.imwrite(final_dir, img)

        else:
            cv2.imwrite(final_dir, img)

    @njit
    def save_njit(self, image_dir, img):
        temp_dir = image_dir.split('/')
        if os.path.exists(final_dir := os.path.join(temp_dir[0], '/'.join(temp_dir[1:]))):
            os.remove(final_dir)
            cv2.imwrite(final_dir, img)

        else:
            cv2.imwrite(final_dir, img)

    # -- Gets the shape of the image as a list. [columns, rows, channels] -- #
    @staticmethod
    def get_image_shape(image) -> tuple:
        return image.shape

    @jit(nopython=False)
    def get_image_shape_jit(self, image) -> tuple:
        return image.shape

    @njit
    def get_image_shape_njit(self, image) -> tuple:
        return image.shape

    # -- Changes a pixel to a new colour -- #
    @staticmethod
    def change_pixel(image, pixel_col: int, pixel_row: int, colour: tuple[int, int, int]):
        image[pixel_col][pixel_row] = list(colour)

    @jit(nopython=False)
    def change_pixel_jit(self, image, pixel_col: int, pixel_row: int, colour: tuple[int, int, int]):
        image[pixel_col][pixel_row] = list(colour)

    @njit
    def change_pixel_njit(self, image, pixel_col: int, pixel_row: int, colour: tuple[int, int, int]):
        image[pixel_col][pixel_row] = list(colour)

    # -- changes a group of pixels to a new colour -- #
    @staticmethod
    def change_pixel_group(image, colour: tuple[int, int, int], rowI=0, colI=0, row_slice=None, col_slice=None):
        if row_slice is None and col_slice is None:
            for i in range(rowI):
                for j in range(colI):
                    image[i][j] = list(colour)

        elif row_slice is not None and col_slice is None:
            for row in range(image[row_slice[0]:row_slice[1]]):
                for j in range(image.shape[1]):
                    image[row][j] = list(colour)

        elif row_slice is None and col_slice is not None:
            for i in range(image.shape[0]):
                for col in range(image[i][col_slice[0]:col_slice[1]]):
                    image[i][col] = list(colour)

        else:
            for col in range(image[col_slice[0]:col_slice[1]]):
                for row in range(image[col][row_slice[0]:row_slice[1]]):
                    image[col][row] = list(colour)

    @jit(nopython=False)
    def change_pixel_group_jit(self, image, colour: tuple[int, int, int], rowI=0, colI=0, row_slice=None,
                               col_slice=None):
        if row_slice is None and col_slice is None:
            for i in range(rowI):
                for j in range(colI):
                    image[i][j] = list(colour)

        elif row_slice is not None and col_slice is None:
            for row in range(image[row_slice[0]:row_slice[1]]):
                for j in range(image.shape[1]):
                    image[row][j] = list(colour)

        elif row_slice is None and col_slice is not None:
            for i in range(image.shape[0]):
                for col in range(image[i][col_slice[0]:col_slice[1]]):
                    image[i][col] = list(colour)

        else:
            for col in range(image[col_slice[0]:col_slice[1]]):
                for row in range(image[col][row_slice[0]:row_slice[1]]):
                    image[col][row] = list(colour)

    @njit
    def change_pixel_group_njit(self, image, colour: tuple[int, int, int], rowI=0, colI=0, row_slice=None,
                                col_slice=None):
        if row_slice is None and col_slice is None:
            for i in range(rowI):
                for j in range(colI):
                    image[i][j] = list(colour)

        elif row_slice is not None and col_slice is None:
            for row in range(image[row_slice[0]:row_slice[1]]):
                for j in range(image.shape[1]):
                    image[row][j] = list(colour)

        elif row_slice is None and col_slice is not None:
            for i in range(image.shape[0]):
                for col in range(image[i][col_slice[0]:col_slice[1]]):
                    image[i][col] = list(colour)

        else:
            for col in range(image[col_slice[0]:col_slice[1]]):
                for row in range(image[col][row_slice[0]:row_slice[1]]):
                    image[col][row] = list(colour)

    # -- copies a slice of the image and pastes it to a new location -- #
    @staticmethod
    def copy_paste_image_section(image, start_col, end_col, size):
        tag = image[start_col:start_col + size]
        image[end_col:end_col + size] = tag

    @jit(nopython=False)
    def copy_paste_image_section_jit(self, image, start_col, end_col, size):
        tag = image[start_col:start_col + size]
        image[end_col:end_col + size] = tag

    @njit
    def copy_paste_image_section_njit(self, image, start_col, end_col, size):
        tag = image[start_col:start_col + size]
        image[end_col:end_col + size] = tag
