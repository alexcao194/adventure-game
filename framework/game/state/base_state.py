from framework.core.logger import log_state
from framework.utils.media_query import *
from framework.game.widget.widget_group import WidgetGroup
from framework.game.entity.entity_group import EntityGroup
import pygame

'''
class BaseState
name: str - the name of the state
background: str - the path to the background image
widgets: WidgetGroup - the widgets of the state
'''

class BaseState:
    def __init__(self, background = ''):
        self.background_asset = background
        self.background_image = None


    '''
    Update is called every frame.
    '''
    def update(self, event):
        pass

    '''
    Render is called every frame. 
    '''
    def render(self, display):
        if(self.background_asset != ''):
            display.blit(self.background_image, (0, 0))
    

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
    def __init__(self, background=''):
        super().__init__(background)