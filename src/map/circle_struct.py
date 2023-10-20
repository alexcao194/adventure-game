from framework.framework import *
from src.configs.assets import Assets

class CircleStruct(Entity):
    def __init__(self, player: Entity):
        super().__init__(hitbox=Vector2(230, 175), position=Vector2(582, 49), size=Vector2(230, 175), offset=Vector2(0, 0))
        self.texture = Texture(texture=Assets.tt_well_0, entity=self)
        self.player = player
        self.is_solid = False
        self.is_active = False
    
    def __update__(self, event):
        for collision in self.collisions:
            if(not self.is_active and collision.__class__.__name__ == "Player"):
                self.texture = Texture(texture=Assets.tt_block_2, entity=self)
                self.is_active = True