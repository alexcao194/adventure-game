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
            'roll': ActionAnimation(Assets.roll, 5, self, delay=2),
            'test': ActionAnimation(Assets.test, 10, self, delay=2),
        },
        {
            'walk': RepeatAnimation(Assets.walk, 8, self, delay=2),
            'idle': RepeatAnimation(Assets.idle, 6, self, delay=2),
            'test2': RepeatAnimation(Assets.test2, 10, self, delay=2),
        },
        'idle'
    )
    
    def update(self, event):
        super().update(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                self.animation_manager.play_action('roll')
                    
            
    def render(self, display):
        super().render(display)
        self.animation_manager.render(display)
        