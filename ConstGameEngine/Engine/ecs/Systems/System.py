import numpy as np


class System:
    def __init__(self, systems=None):
        if systems is None:
            self.systems = np.array([], dtype=object)

        else:
            self.systems = systems

    def get_systems(self):
        return self.systems

    def set_systems(self, systems):
        self.systems = systems

    def connect(self, entity):
        entity.set_systems(self.systems)
