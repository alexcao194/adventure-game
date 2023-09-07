from framework.utils.vector2 import Vector2
import pygame

'''
Widget is the base class for all widgets.
position: Vector2 - the position of the widget
size: Vector2 - the size of the widget
'''

class Widget:
    def __init__(self, position: Vector2, size: Vector2):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position.to_tuple(), size)
    
    def render(self, display):
        pass

    def update(self, event):
        pass