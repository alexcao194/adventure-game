from framework.game.widget.widget import Widget
from framework.utils.vector2 import Vector2
import pygame

class Image(Widget):
    '''
    Image is a widget that displays an image.
    image: str - the image to display
    '''
    
    def __init__(self, src: str = None, position: Vector2 = None, size: Vector2 = None, scale: Vector2 = Vector2(1, 1)):
        if(src == None):
            raise Exception("Image must have an image")
        if(not scale.is_positive()):
            raise Exception("Scale must be positive")
        super().__init__(position=position, size=size)
        self.image = src
        self.scale = scale
        self.init()
    
    def init(self):
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale.x), int(self.image.get_height() * self.scale.y)))
        self.size = Vector2(self.image.get_size()[0], self.image.get_size()[1])
    
    def render(self, display):
        display.blit(self.image, (self.position.x + self.size.x / 2 - self.image.get_width() / 2, self.position.y + self.size.y / 2 - self.image.get_height() / 2))
    