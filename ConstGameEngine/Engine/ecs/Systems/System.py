import numpy as np
from numba import jit, njit


class System:
    def __init__(self, systems=None):
        if systems is None:
            self.systems = np.array([], dtype=object)

        else:
            self.systems = systems

    def get_systems(self):
        return self.systems

    @jit(nopython=False)
    def get_systems_jit(self):
        return self.systems

    @njit
    def get_systems_njit(self):
        return self.systems

    def set_systems(self, systems):
        self.systems = systems

    @jit(nopython=False)
    def set_systems_jit(self, systems):
        self.systems = systems

    @njit
    def set_systems_njit(self, systems):
        self.systems = systems

    def connect(self, entity):
        entity.set_systems(self.systems)

    @jit(nopython=False)
    def connect_jit(self, entity):
        entity.set_systems(self.systems)

    @njit
    def connect_njit(self, entity):
        entity.set_systems(self.systems)
