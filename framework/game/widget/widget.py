from framework.utils.vector2 import Vector2
import pygame

class Widget:
    def __init__(self, key, position: Vector2, size: Vector2):
        self.key = key
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position.to_tuple(), size)
    
    def render(self, display):
        pass

    def update(self, event):
        pass