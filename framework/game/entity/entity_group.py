from framework.game.entity.entity import *


class EntityGroup:
    '''
    EntityGroup is a group of entities.
    entities: list - the list of entities
    '''
    def __init__(self):
        self.entities = []
    
    def add(self, entity: Entity):
        self.entities.append(entity)
    
    def remove(self, entity: Entity):
        self.entities.remove(entity)
    
    def __render__(self, display):
        for entity in self.entities:
            entity.__render__(display)
    def __update__(self, event):
        for entity in self.entities:
            entity.__update__(event)