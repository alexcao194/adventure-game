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
        self.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.animation_manager.play_action('roll')
            
            if event.key == pygame.K_x:
                self.animation_manager.play_action('test')

            if event.key == pygame.K_c:
                self.animation_manager.change_animation('test2')
            
        
                    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position.x -= 5
            self.animation_manager.change_animation('walk')
        elif keys[pygame.K_RIGHT]:
            self.position.x += 5
            self.animation_manager.change_animation('walk')
        else:
            self.animation_manager.change_animation('idle')

    def render(self, display):
        super().render(display)
        self.animation_manager.render(display)
        