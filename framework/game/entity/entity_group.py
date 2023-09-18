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
    
    def render(self, display):
        for entity in self.entities:
            entity.render(display)
    def update(self, event):
        for entity in self.entities:
            entity.update(event)