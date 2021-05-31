from numba import jit, njit


# -- Create class - #
class Colour:
    # -- Constructor -- #
    def __init__(self, RGB: tuple[int, int, int]):
        self.__RGB = RGB
        self.__red = RGB[0]
        self.__green = RGB[1]
        self.__blue = RGB[2]

    # -- Allows the user to change the RGB values of the colour -- #
    def set_RGB(self, newRGB):
        self.__RGB = newRGB
        self.__red = newRGB[0]
        self.__green = newRGB[1]
        self.__blue = newRGB[2]

    @jit(nopython=False)
    def set_RGB_jit(self, newRGB):
        self.__RGB = newRGB
        self.__red = newRGB[0]
        self.__green = newRGB[1]
        self.__blue = newRGB[2]

    @njit
    def set_RGB_njit(self, newRGB):
        self.__RGB = newRGB
        self.__red = newRGB[0]
        self.__green = newRGB[1]
        self.__blue = newRGB[2]

    # -- Below methods are all getters -- #
    def get_RGB(self) -> tuple[int, int, int]:
        return self.__RGB

    @jit(nopython=False)
    def get_RGB_jit(self) -> tuple[int, int, int]:
        return self.__RGB

    @njit
    def get_RGB_njit(self) -> tuple[int, int, int]:
        return self.__RGB

    def get_red(self) -> int:
        return self.__red

    @jit(nopython=False)
    def get_red_jit(self) -> int:
        return self.__red

    @njit
    def get_red_njit(self) -> int:
        return self.__red

    def get_green(self) -> int:
        return self.__green

    @jit(nopython=False)
    def get_green_jit(self) -> int:
        return self.__green

    @njit
    def get_green_njit(self) -> int:
        return self.__green

    def get_blue(self) -> int:
        return self.__blue

    @jit(nopython=False)
    def get_blue_jit(self) -> int:
        return self.__blue

    @njit
    def get_blue_njit(self) -> int:
        return self.__blue
