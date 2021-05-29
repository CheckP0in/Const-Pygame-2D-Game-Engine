import numpy as np


# -- Create class -- #
class Vector1D:
    # -- Constructor -- #
    def __init__(self, x):
        self.__x = x
        self.__vector = np.array([], dtype=np.float)

    # -- Initialize the vector -- #
    def init(self):
        self.__vector = np.append(self.__vector, self.__x)

    # -- return the vector -- #
    def get_vector(self) -> np.array:
        return self.__vector

    # -- set the vector to a new value -- #
    def set_vector(self, v: np.array):
        self.__vector = v

    # -- get the 'x' axis of the vector -- #
    def get_x(self) -> float:
        return self.__x

    # -- set the 'x' axis to a new value -- #
    def set_x(self, x):
        self.__x = x


# -- Create class -- #
class Vector2D:
    # -- Constructor -- #
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__vector = np.array([], dtype=np.float)

    # -- Initialize the vector -- #
    def init(self):
        self.__vector = np.append(self.__vector, self.__x)
        self.__vector = np.append(self.__vector, self.__y)

    # -- return the vector -- #
    def get_vector(self) -> np.array:
        return self.__vector

    # -- set the vector to a new value -- #
    def set_vector(self, v: np.array):
        self.__vector = v

    # -- get the 'x' axis of the vector -- #
    def get_x(self) -> float:
        return self.__x

    # -- set the 'x' axis to a new value -- #
    def set_x(self, x):
        self.__x = x

    # -- get the 'y' axis of the vector -- #
    def get_y(self) -> float:
        return self.__y

    # -- set the 'y' axis to a new value -- #
    def set_y(self, y):
        self.__y = y
