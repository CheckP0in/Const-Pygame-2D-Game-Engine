from threading import Thread
from multiprocessing import Process
import numpy as np


class Entity:
    def __init__(self):
        self.component = None
        self.systems = np.array([], dtype=object)

    def set_component(self, component):
        self.component = component

    def get_component(self):
        return self.component

    def set_systems(self, systems):
        self.systems = systems

    def get_systems(self):
        return self.systems

    def add_system(self, system):
        np.append(self.systems, system)

    def insert_system(self, ind, system):
        np.insert(self.systems, ind, system)

    def remove_system(self, system):
        np.remove(self.systems, system)

    def silent_remove_system(self, system):
        if system in self.systems:
            np.remove(self.systems, system)

    def run(self):
        for system in self.systems:
            system()

    def run_concurrent(self, join=False, daemon=False):
        for system in self.systems:
            t = Thread(target=system)
            t.start()

            if join:
                t.join()

            if daemon:
                t.daemon = True

    def run_parallel(self, join=False, daemon=False):
        for system in self.systems:
            p = Process(target=system)
            p.start()

            if join:
                p.join()

            if daemon:
                p.daemon = True
