from framework.game.widget.widget import Widget
from framework.utils.media_query import MediaQuery
import pygame

class Text(Widget):
    def __init__(self, position, size, text, font: str = MediaQuery.font_family, font_size: int = MediaQuery.font_size, color: tuple = (255, 255, 255)):
        super().__init__(position, size)
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.color = color
    
    def render(self, display):
        text = self.font.render(self.text, True, self.color)
        display.blit(text, (self.position.x + self.size.x / 2 - text.get_width() / 2, self.position.y + self.size.y / 2 - text.get_height() / 2))
