import numpy as np


class EntityManager:
    def __init__(self, entities=None):
        if entities is None:
            self.entities = np.array([], dtype=object)

        else:
            self.entities = np.array(entities, dtype=object)

    def get_entities(self):
        return self.entities

    def set_entities(self, entities):
        self.entities = entities

    def is_entity_in_list(self, ent):
        return ent in self.entities

    def remove_entity(self, entity):
        np.remove(self.entities, entity)

    def silent_remove_entity(self, entity):
        if entity in self.entities:
            np.remove(self.entities, entity)

    def add_entity(self, entity):
        np.append(self.entities, entity)

    def insert_entity(self, ind, entity):
        np.insert(self.entities, ind, entity)
