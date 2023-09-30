import pygame
from framework.utils.vector2 import Vector2


class Entity:
    '''
    Entity is the base class for all game objects.
    position: Vector2 - the position of the entity
    hitbox: Vector2 - the size of the entity and the hitbox
    '''
    def __init__(self, position: Vector2, hitbox:Vector2):
        if(self.__class__.__name__ == 'Entity'):
            raise Exception("Entity cannot be instantiated")
        self.position = position
        self.hitbox = hitbox
        self.rect = pygame.Rect(position.to_tuple(), hitbox.to_tuple())
        self.isActive = True
        self.fliped = False
    
    def render(self, display):
        pass

    def update(self, event):
        if(self.isActive == False):
            raise Exception("Entity is not active")
            

    def is_colliding(self, other):
        return self.rect.colliderect(other.rect)


        