import pygame
from framework.utils.vector2 import Vector2
from framework.game.animations.animation import Animation

class Entity:
    def __init__(self, key, position: Vector2, hitbox:Vector2):
        self.key = key
        self.position = position
        self.hitbox = hitbox
        self.rect = pygame.Rect(position.to_tuple(), hitbox.to_tuple())
    
    def render(self, display):
        pass

    def update(self, event):
        pass


        