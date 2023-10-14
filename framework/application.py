import pygame
from framework.utils.vector2 import Vector2
from framework.utils.clock import Clock
from framework.game.state.base_state import BaseState
from framework.game.state.state_machine import StateMachine
from framework.utils.media_query import MediaQuery
from framework.core.localization import Localization

class Application:
    """
    Application class is the main class of the framework.
    It is responsible for creating the window and running the game loop.
    vector2 is a Vector2 object that represents the size of the window.
    """
    display = None
    clock = None
    isActive = False
    def __init__(self) -> None:
        self.display = pygame.display.set_mode(MediaQuery.size.to_tuple())
        self.clock = pygame.time.Clock()
        self.isActive = True
        self.__current_language__ = 'en'
        pygame.init()
        
    def init_state(self, init_state: BaseState):
        StateMachine.push(init_state)

    def run(self):
        """
        This method is responsible for running the game loop.
        """
        while self.isActive:
            self.handle_events()
            self.__render__(self.display)
    '''
    This method is responsible for updating the game.
    '''
    def __update__(self, event):
        Clock.__update__(event)
        if(self.__current_language__ != Localization.language):
            self.__current_language__ = Localization.language
            StateMachine.__rebuild_stack__()
        StateMachine.__current_state__().__update__(event)

    def __render__(self, display):
        StateMachine.__current_state__().__render__(display)
        pygame.display.flip()

    """
    This method is responsible for handling the events.
    """
    def handle_events(self):
        updated = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isActive = False
                pygame.quit()
                quit()
            else:
                self.__update__(event)
            updated = True
        if not updated:
            self.__update__(pygame.event.Event(pygame.NOEVENT))
