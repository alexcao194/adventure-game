from framework.framework import *
from framework.utils.vector2 import Vector2
from src.configs.assets import Assets

class Player(Entity):
    animations = None
    def __init__(self, key, position: Vector2, hitbox: Vector2):
        super().__init__(key, position, hitbox)
        self.animations = [
            Animation("walk", Assets.test, 8, self, delay=2)
        ]

    def render(self, display):
        super().render(display)
        self.animations[0].render(display)