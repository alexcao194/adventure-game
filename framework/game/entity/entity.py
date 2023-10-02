import pygame
from framework.utils.vector2 import Vector2


class Entity:
    '''
    Entity is the base class for all game objects.
    position: Vector2 - the position of the entity
    hitbox: Vector2 - the size of the entity and the hitbox
    '''
    def __init__(self, hitbox: Vector2 = None, position: Vector2 = None, animation_manager = None, texture = None):
        if(self.__class__.__name__ == 'Entity'):
            raise Exception("Entity cannot be instantiated")
        if(animation_manager == None and texture == None):
            raise Exception("Entity must have either animation_manager or texture")
        if(animation_manager != None and texture != None):
            raise Exception("Entity cannot have both animation_manager and texture")
        if(position == None):
            raise Exception("Entity must have a position")
        if(hitbox == None):
            raise Exception("Entity must have a hitbox")
        if(not hitbox.is_positive()):
            raise Exception("Hitbox must be positive")
        self.position = position
        self.hitbox = hitbox
        self.rect = pygame.Rect(position.to_tuple(), hitbox.to_tuple())
        self.isActive = True
        self.fliped = False
        self.animation_manager = animation_manager
        self.texture = texture
    
    def render(self, display):
        if(self.isActive == False):
            return
        if(self.animation_manager != None):
            self.animation_manager.render(display)
        elif(self.texture != None):
            self.texture.render(display)
        else:
            raise Exception("Entity must have either animation_manager or texture")

    def update(self, event):
        if(self.isActive == False):
            return
        if(self.animation_manager != None):
            self.animation_manager.update(event)
        elif(self.texture != None):
            self.texture.update(event)
        else:
            raise Exception("Entity must have either animation_manager or texture")
            

    def is_colliding(self, other):
        return self.rect.colliderect(other.rect)


        