import pygame
from framework.utils.vector2 import Vector2

'''
Entity is the base class for all game objects.
position: Vector2 - the position of the entity
hitbox: Vector2 - the size of the entity and the hitbox
'''
class Entity:
    def __init__(self, position: Vector2, hitbox:Vector2):
        self.position = position
        self.hitbox = hitbox
        self.rect = pygame.Rect(position.to_tuple(), hitbox.to_tuple())
    
    def render(self, display):
        pass

    def update(self, event):
        pass

    def is_colliding(self, other):
        return self.rect.colliderect(other.rect)


        