import numpy as np
from numba import jit, njit


# -- Create class -- #
class Vector1D:
    # -- Constructor -- #
    def __init__(self, x):
        self.__x = x
        self.__vector = np.array([], dtype=np.float)

    # -- Initialize the vector -- #
    def init(self):
        self.__vector = np.append(self.__vector, self.__x)

    @jit(nopython=False)
    def init_jit(self):
        self.__vector = np.append(self.__vector, self.__x)

    @njit
    def init_njit(self):
        self.__vector = np.append(self.__vector, self.__x)

    # -- return the vector -- #
    def get_vector(self) -> np.array:
        return self.__vector

    @jit(nopython=False)
    def get_vector_jit(self) -> np.array:
        return self.__vector

    @njit
    def get_vector_njit(self) -> np.array:
        return self.__vector

    # -- set the vector to a new value -- #
    def set_vector(self, v: np.array):
        self.__vector = v

    @jit(nopython=False)
    def set_vector_jit(self, v: np.array):
        self.__vector = v

    @njit
    def set_vector_njit(self, v: np.array):
        self.__vector = v

    # -- get the 'x' axis of the vector -- #
    def get_x(self) -> float:
        return self.__x

    @jit(nopython=False)
    def get_x_jit(self) -> float:
        return self.__x

    @njit
    def get_x_njit(self) -> float:
        return self.__x

    # -- set the 'x' axis to a new value -- #
    def set_x(self, x):
        self.__x = x

    @jit(nopython=False)
    def set_x_jit(self, x):
        self.__x = x

    @njit
    def set_x_njit(self, x):
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

    @jit(nopython=False)
    def init_jit(self):
        self.__vector = np.append(self.__vector, self.__x)
        self.__vector = np.append(self.__vector, self.__y)

    @njit
    def init_njit(self):
        self.__vector = np.append(self.__vector, self.__x)
        self.__vector = np.append(self.__vector, self.__y)

    # -- return the vector -- #
    def get_vector(self) -> np.array:
        return self.__vector

    @jit(nopython=False)
    def get_vector_jit(self) -> np.array:
        return self.__vector

    @njit
    def get_vector_njit(self) -> np.array:
        return self.__vector

    # -- set the vector to a new value -- #
    def set_vector(self, v: np.array):
        self.__vector = v

    @jit(nopython=False)
    def set_vector_jit(self, v: np.array):
        self.__vector = v

    @njit
    def set_vector_njit(self, v: np.array):
        self.__vector = v

    # -- get the 'x' axis of the vector -- #
    def get_x(self) -> float:
        return self.__x

    @jit(nopython=False)
    def get_x_jit(self) -> float:
        return self.__x

    @njit
    def get_x_njit(self) -> float:
        return self.__x

    # -- set the 'x' axis to a new value -- #
    def set_x(self, x):
        self.__x = x

    @jit(nopython=False)
    def set_x_jit(self, x):
        self.__x = x

    @njit
    def set_x_njit(self, x):
        self.__x = x

    # -- get the 'y' axis of the vector -- #
    def get_y(self) -> float:
        return self.__y

    @jit(nopython=False)
    def get_y_jit(self) -> float:
        return self.__y

    @njit
    def get_y_njit(self) -> float:
        return self.__y

    # -- set the 'y' axis to a new value -- #
    def set_y(self, y):
        self.__y = y

    @jit(nopython=False)
    def set_y_jit(self, y):
        self.__y = y

    @njit
    def set_y_njit(self, y):
        self.__y = y
