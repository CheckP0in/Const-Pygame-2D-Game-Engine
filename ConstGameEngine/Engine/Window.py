import pygame
from ConstGameEngine.Singleton import Singleton

pygame.init()


@Singleton  # -- Sets the class to be a singleton -- #
class Window:  # -- Create the class -- #
    # -- Constructor -- #
    def __init__(self):
        self.__size = None
        self.__width = int()
        self.__height = int()
        self.__title = str()
        self.__icon = None
        self.__window = None

    # -- Below methods are all getters and setters -- #
    def set_size(self, size: tuple[int, int]):
        self.__size = size
        self.__width = size[0]
        self.__height = size[1]

    def get_size(self) -> tuple[int, int]:
        return self.__size

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def set_title(self, title: str):
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_icon(self, icon):
        self.__icon = icon

    def get_icon(self):
        return self.__icon

    def get_window(self):
        return self.__window

    # -- Initialize the window -- #
    def init(self):
        self.__window = pygame.display.set_mode(self.__size)

        if self.__title is not None:
            pygame.display.set_caption(self.__title)

        if self.__icon is not None:
            pygame.display.set_icon(self.__icon)
