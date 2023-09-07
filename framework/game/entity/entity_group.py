from framework.game.entity.entity import *


'''
EntityGroup is a group of entities.
name: str - the name of the Entity group
entities: list - the list of entities
'''
class EntityGroup:
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