from framework.game.entity.entity import *


class EntityGroup:
    '''
    EntityGroup is a group of entities.
    entities: list - the list of entities
    '''
    def __init__(self):
        self.entities = []
    
    def add(self, Entity: Entity):
        self.entities.append(Entity)
    
    def remove(self, Entity: Entity):
        self.entities.remove(Entity)
    
    def render(self, display):
        for Entity in self.entities:
            Entity.render(display)
    def update(self, event):
        for Entity in self.entities:
            Entity.update(event) 