import pygame
from framework.utils.vector2 import Vector2
from framework.game.state.base_state import BaseState
from framework.game.state.state_machine import StateMachine

class Application:
    """
    Application class is the main class of the framework.
    It is responsible for creating the window and running the game loop.
    vector2 is a Vector2 object that represents the size of the window.
    """
    display = None
    clock = None
    isActive = False
    def __init__(self, vector2: Vector2, init_state: BaseState) -> None:
        self.display = pygame.display.set_mode(vector2.to_tuple())
        self.clock = pygame.time.Clock()
        StateMachine.push(init_state)
        self.isActive = True
    
    def run(self):
        """
        This method is responsible for running the game loop.
        """
        while self.isActive:
            self.clock.tick(60)
            self.handle_events()
            self.render(self.display)
    '''
    This method is responsible for updating the game.
    '''
    def update(self, event):
        StateMachine.current_state().update(event)

    def render(self, display):
        StateMachine.current_state().render(display)
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
                self.update(event)
            updated = True
        if not updated:
            self.update(pygame.event.Event(pygame.NOEVENT))
