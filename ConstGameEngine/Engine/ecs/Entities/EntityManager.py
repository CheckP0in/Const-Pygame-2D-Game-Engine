class EntityManager:
    def __init__(self, entities=None):
        if entities is None:
            self.entities = list()

        else:
            self.entities = entities

    def get_entities(self):
        return self.entities

    def set_entities(self, entities):
        self.entities = entities

    def is_entity_in_list(self, ent):
        return ent in self.entities

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def silent_remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def add_entity(self, entity):
        self.entities.append(entity)

    def insert_entity(self, ind, entity):
        self.entities.insert(ind, entity)
