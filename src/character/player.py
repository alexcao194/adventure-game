from framework.framework import *
from framework.utils.vector2 import Vector2
from src.configs.assets import Assets
import pygame

class Player(Entity):
    animations = None
    current_animation = 'test2'
    def __init__(self, position: Vector2, hitbox: Vector2):
        super().__init__(position, hitbox)
        self.animations = {
            'test' : ActionAnimation("test", Assets.test, 8, self, delay=2),
            'test2' : RepeatAnimation("test2", Assets.test2, 10, self, delay=2)
        }
    
    def update(self, event):
        super().update(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if(self.current_animation == 'test2'):
                    self.current_animation = 'test'
                    self.animations[self.current_animation].reset()

        if(type(self.animations[self.current_animation]) == ActionAnimation and not self.animations[self.current_animation].isStart):
            self.current_animation = 'test2'
            self.animations[self.current_animation].reset()
            
    def render(self, display):
        super().render(display)
        self.animations[self.current_animation].render(display)
        