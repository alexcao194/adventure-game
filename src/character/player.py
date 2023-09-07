from framework.framework import *
from framework.utils.vector2 import Vector2
from src.configs.assets import Assets
import pygame

class Player(Entity):
    animation_manager = None
    def __init__(self, position: Vector2, hitbox: Vector2):
        super().__init__(position, hitbox)
        self.animation_manager = AnimationManager(
        {
            'test2' : ActionAnimation(Assets.test, 8, self, delay=2),
        },
        {
            'test' : RepeatAnimation(Assets.test2, 10, self, delay=2),
        },
        'test'
    )
    
    def update(self, event):
        super().update(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if (self.animation_manager.current_action_animation == None):
                    self.animation_manager.play_action('test2')
            
    def render(self, display):
        super().render(display)
        self.animation_manager.render(display)
        