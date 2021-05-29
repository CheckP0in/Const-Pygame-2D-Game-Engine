from threading import Thread
from multiprocessing import Process
import numpy as np
from numba import jit, njit


class Entity:
    def __init__(self):
        self.component = None
        self.systems = np.array([], dtype=object)

    def set_component(self, component):
        self.component = component

    @jit(nopython=False)
    def set_component_jit(self, component):
        self.component = component

    @njit
    def set_component_njit(self, component):
        self.component = component

    def get_component(self):
        return self.component

    @jit(nopython=False)
    def get_component_jit(self):
        return self.component

    @njit
    def get_component_njit(self):
        return self.component

    def set_systems(self, systems):
        self.systems = systems

    @jit(nopython=False)
    def set_systems_jit(self, systems):
        self.systems = systems

    @njit
    def set_systems_njit(self, systems):
        self.systems = systems

    def get_systems(self):
        return self.systems

    @jit(nopython=False)
    def get_systems_jit(self):
        return self.systems

    @njit
    def get_systems_njit(self):
        return self.systems

    def add_system(self, system):
        np.append(self.systems, system)

    @jit(nopython=False)
    def add_system_jit(self, system):
        np.append(self.systems, system)

    @njit
    def add_system_njit(self, system):
        np.append(self.systems, system)

    def insert_system(self, ind, system):
        np.insert(self.systems, ind, system)

    @jit(nopython=False)
    def insert_system_jit(self, ind, system):
        np.insert(self.systems, ind, system)

    @njit
    def insert_system_njit(self, ind, system):
        np.insert(self.systems, ind, system)

    def remove_system(self, system):
        np.remove(self.systems, system)

    @jit(nopython=False)
    def remove_system_jit(self, system):
        np.remove(self.systems, system)

    @njit
    def remove_system_njit(self, system):
        np.remove(self.systems, system)

    def silent_remove_system(self, system):
        if system in self.systems:
            np.remove(self.systems, system)

    @jit(nopython=False)
    def silent_remove_system_jit(self, system):
        if system in self.systems:
            np.remove(self.systems, system)

    @njit
    def silent_remove_system_njit(self, system):
        if system in self.systems:
            np.remove(self.systems, system)

    def run(self):
        for system in self.systems:
            system()

    @jit(nopython=False)
    def run_jit(self):
        for system in self.systems:
            system()

    @njit
    def run_njit(self):
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

    @jit(nopython=False)
    def run_concurrent_jit(self, join=False, daemon=False):
        for system in self.systems:
            t = Thread(target=system)
            t.start()

            if join:
                t.join()

            if daemon:
                t.daemon = True

    @njit
    def run_concurrent_njit(self, join=False, daemon=False):
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

    @jit(nopython=False)
    def run_parallel_jit(self, join=False, daemon=False):
        for system in self.systems:
            p = Process(target=system)
            p.start()

            if join:
                p.join()

            if daemon:
                p.daemon = True

    @njit
    def run_parallel_njit(self, join=False, daemon=False):
        for system in self.systems:
            p = Process(target=system)
            p.start()

            if join:
                p.join()

            if daemon:
                p.daemon = True
