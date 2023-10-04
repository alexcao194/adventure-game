from framework.core.logger import log
from framework.utils.media_query import *
from framework.game.widget.widget_group import WidgetGroup
from framework.game.entity.entity_group import EntityGroup
import pygame

class BaseState:
    '''
    class BaseState
    background: str - the path to the background image
    '''
    def __init__(self, background: str = None):
        if(self.__class__.__name__ == 'BaseState'):
            raise Exception("BaseState cannot be instantiated")
        if(background == None):
            raise Exception("BaseState must have a background")
        self.background_asset = background
        self.background_image = None
        self.widget_group = WidgetGroup()
        self.entity_group = EntityGroup()



    def update(self, event):
        '''
        Update is called every frame.
        '''
        self.widget_group.update(event)
        self.entity_group.update(event)

    
    def render(self, display):
        '''
        Render is called every frame. 
        '''
        if(self.background_asset != ''):
            display.blit(self.background_image, (0, 0))
        self.widget_group.render(display)
        self.entity_group.render(display)
    

    
    def destroy(self):
        '''
        Destroy is called when the state is destroyed.
        '''
        log(self, "Destroyed")

    
    def init(self):
        '''
        Init is called when the state is created.
        '''
        self.background_image = pygame.image.load(self.background_asset)
        width = self.background_image.get_width()
        height = self.background_image.get_height()
        # transform with original aspect ratio
        if(width < MediaQuery.size.x):
            self.background_image = pygame.transform.scale(self.background_image, (MediaQuery.size.x, (MediaQuery.size.x / width) * height))
        if(height < MediaQuery.size.y):
            self.background_image = pygame.transform.scale(self.background_image, ((MediaQuery.size.y / height) * width, MediaQuery.size.y))
        log(self, "Initialized")
    
class FallState(BaseState):
    def __init__(self, background=''):
        super().__init__(background)