from framework.core.logger import log_state
from framework.utils.media_query import *
from framework.game.widget.widget_group import WidgetGroup
import pygame

class BaseState:
    def __init__(self, name, background = '', widgets: WidgetGroup = WidgetGroup("no widget", [])):
        self.name = name
        self.background_asset = background
        self.background_image = None
        self.widgets = widgets


    '''
    Update is called every frame.
    '''
    def update(self, event):
        self.widgets.update(event)


    '''
    Render is called every frame. 
    '''
    def render(self, display):
        if(self.background_asset != ''):
            display.blit(self.background_image, (0, 0))
        self.widgets.render(display)

    '''
    Destroy is called when the state is destroyed.
    '''
    def destroy(self):
        log_state(self, "Destroyed")

    '''
    Init is called when the state is created.
    '''
    def init(self):
        self.background_image = pygame.image.load(self.background_asset)
        width = self.background_image.get_width()
        height = self.background_image.get_height()
        # transform with original aspect ratio
        if(width < MediaQuery.size.x):
            self.background_image = pygame.transform.scale(self.background_image, (MediaQuery.size.x, (MediaQuery.size.x / width) * height))
        if(height < MediaQuery.size.y):
            self.background_image = pygame.transform.scale(self.background_image, ((MediaQuery.size.y / height) * width, MediaQuery.size.y))
        log_state(self, "Initialized")
    
class FallState(BaseState):
    def __init__(self, name, background='', widgets: WidgetGroup = WidgetGroup("no widget", [])):
        super().__init__(name, background, widgets)