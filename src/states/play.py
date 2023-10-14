from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player

class Play(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()

        self.player = Player(position=Vector2(160, 421))

        self.entity_group.add(self.player)
    