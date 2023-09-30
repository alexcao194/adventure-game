from framework.game.widget.widget import Widget
from framework.utils.vector2 import Vector2
import pygame

class Image(Widget):
    '''
    Image is a widget that displays an image.
    image: str - the image to display
    '''
    
    def __init__(self, position, src, scale: Vector2 = Vector2(1, 1)):
        super().__init__(position, Vector2(0, 0))
        self.image = src
        self.scale = scale
        self.init()
    
    def init(self):
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale.x), int(self.image.get_height() * self.scale.y)))
    
    def render(self, display):
        display.blit(self.image, self.position.to_tuple())
    