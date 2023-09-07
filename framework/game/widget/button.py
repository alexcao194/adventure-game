from framework.utils.vector2 import Vector2
from framework.game.widget.widget import Widget
import pygame


class Button(Widget):
    '''
    Button is a widget that can be clicked.
    callback: callable - the function that is called when the button is clicked
    '''
    def __init__(self, position: Vector2, size: Vector2, callback: callable):
        super().__init__(position, size)
        self.callback = callback

    def update(self, event):
        self.handle_events(event)
        
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.callback()
                return True
        return False
    

class ImageButton(Button):
    '''
    ImageButton is a button that has an image as background.
    background: str - the path to the background image
    '''
    def __init__(self, position: Vector2, background: str, callback, scale = 1):
        self.image = pygame.image.load(background)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        super().__init__(position, self.image.get_size(), callback)
    
    def render(self, display):
        display.blit(self.image, self.position.to_tuple())
        
