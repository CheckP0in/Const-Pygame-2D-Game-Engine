import pygame
from ConstGameEngine.Singleton import Singleton
from numba import jit, njit

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

    @jit(nopython=False)
    def set_size_jit(self, size: tuple[int, int]):
        self.__size = size
        self.__width = size[0]
        self.__height = size[1]

    @njit
    def set_size_njit(self, size: tuple[int, int]):
        self.__size = size
        self.__width = size[0]
        self.__height = size[1]

    def get_size(self) -> tuple[int, int]:
        return self.__size

    @jit(nopython=False)
    def get_size_jit(self) -> tuple[int, int]:
        return self.__size

    @njit
    def get_size_njit(self) -> tuple[int, int]:
        return self.__size

    def get_width(self) -> int:
        return self.__width

    @jit(nopython=False)
    def get_width_jit(self) -> int:
        return self.__width

    @njit
    def get_width_njit(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    @jit(nopython=False)
    def get_height_jit(self) -> int:
        return self.__height

    @njit
    def get_height_njit(self) -> int:
        return self.__height

    def set_title(self, title: str):
        self.__title = title

    @jit(nopython=False)
    def set_title_jit(self, title: str):
        self.__title = title

    @njit
    def set_title_njit(self, title: str):
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    @jit(nopython=False)
    def get_title_jit(self) -> str:
        return self.__title

    @njit
    def get_title_njit(self) -> str:
        return self.__title

    def set_icon(self, icon):
        self.__icon = icon

    @jit(nopython=False)
    def set_icon_jit(self, icon):
        self.__icon = icon

    @njit
    def set_icon_njit(self, icon):
        self.__icon = icon

    def get_icon(self):
        return self.__icon

    @jit(nopython=False)
    def get_icon_jit(self):
        return self.__icon

    @njit
    def get_icon_njit(self):
        return self.__icon

    def get_window(self):
        return self.__window

    @jit(nopython=False)
    def get_window_jit(self):
        return self.__window

    @njit
    def get_window_njit(self):
        return self.__window

    # -- Initialize the window -- #
    def init(self):
        self.__window = pygame.display.set_mode(self.__size)

        if self.__title is not None:
            pygame.display.set_caption(self.__title)

        if self.__icon is not None:
            pygame.display.set_icon(self.__icon)

    @jit(nopython=False)
    def init_jit(self):
        self.__window = pygame.display.set_mode(self.__size)

        if self.__title is not None:
            pygame.display.set_caption(self.__title)

        if self.__icon is not None:
            pygame.display.set_icon(self.__icon)

    @njit
    def init_njit(self):
        self.__window = pygame.display.set_mode(self.__size)

        if self.__title is not None:
            pygame.display.set_caption(self.__title)

        if self.__icon is not None:
            pygame.display.set_icon(self.__icon)
