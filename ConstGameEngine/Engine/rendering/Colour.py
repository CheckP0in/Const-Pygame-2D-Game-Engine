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

    # -- Below methods are all getters -- #
    def get_RGB(self) -> tuple[int, int, int]:
        return self.__RGB

    def get_red(self) -> int:
        return self.__red

    def get_green(self) -> int:
        return self.__green

    def get_blue(self) -> int:
        return self.__blue
