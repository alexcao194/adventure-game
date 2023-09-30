from framework.utils.vector2 import Vector2
from framework.game.widget.widget import Widget
from framework.utils.media_query import MediaQuery
import pygame


class Button(Widget):
    '''
    Button is a widget that can be clicked.
    callback: callable - the function that is called when the button is clicked
    '''
    def __init__(self, position: Vector2, size: Vector2, callback: callable, text: str, font = MediaQuery.font_family, font_size: int = MediaQuery.font_size):
        super().__init__(position, size)
        self.callback = callback
        self.font = pygame.font.Font(font, font_size)
        self.text = text

    def render(self, display):
        if self.text:
            text = self.font.render(self.text, True, (255, 255, 255))
            display.blit(text, (self.position.x + self.size.x / 2 - text.get_width() / 2, self.position.y + self.size.y / 2 - text.get_height() / 2))

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
    def __init__(self, position: Vector2, background: str, callback, scale = 1, text = None, font = MediaQuery.font_family, font_size: int = MediaQuery.font_size):
        self.image = pygame.image.load(background)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        super().__init__(position, Vector2(self.image.get_size()[0], self.image.get_size()[1]), callback, text, font, font_size)
    
    def render(self, display):
        display.blit(self.image, self.position.to_tuple())
        super().render(display)
        
