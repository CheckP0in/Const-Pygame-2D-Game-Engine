import numpy as np
from numba import jit, njit


class EntityManager:
    def __init__(self, entities=None):
        if entities is None:
            self.entities = np.array([], dtype=object)

        else:
            self.entities = np.array(entities, dtype=object)

    def get_entities(self):
        return self.entities

    @jit(nopython=False)
    def get_entities_jit(self):
        return self.entities

    @njit
    def get_entities_njit(self):
        return self.entities

    def set_entities(self, entities):
        self.entities = entities

    @jit(nopython=False)
    def set_entities_jit(self, entities):
        self.entities = entities

    @njit
    def set_entities_njit(self, entities):
        self.entities = entities

    def is_entity_in_list(self, ent):
        return ent in self.entities

    @jit(nopython=False)
    def is_entity_in_list_jit(self, ent):
        return ent in self.entities

    @njit
    def is_entity_in_list_njit(self, ent):
        return ent in self.entities

    def remove_entity(self, entity):
        np.remove(self.entities, entity)

    @jit(nopython=False)
    def remove_entity_jit(self, entity):
        np.remove(self.entities, entity)

    @njit
    def remove_entity_njit(self, entity):
        np.remove(self.entities, entity)

    def silent_remove_entity(self, entity):
        if entity in self.entities:
            np.remove(self.entities, entity)

    @jit(nopython=False)
    def silent_remove_entity_jit(self, entity):
        if entity in self.entities:
            np.remove(self.entities, entity)

    @njit
    def silent_remove_entity_njit(self, entity):
        if entity in self.entities:
            np.remove(self.entities, entity)

    def add_entity(self, entity):
        np.append(self.entities, entity)

    @jit(nopython=False)
    def add_entity_jit(self, entity):
        np.append(self.entities, entity)

    @njit
    def add_entity_njit(self, entity):
        np.append(self.entities, entity)

    def insert_entity(self, ind, entity):
        np.insert(self.entities, ind, entity)

    @jit(nopython=False)
    def insert_entity_jit(self, ind, entity):
        np.insert(self.entities, ind, entity)

    @njit
    def insert_entity_njit(self, ind, entity):
        np.insert(self.entities, ind, entity)
