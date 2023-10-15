from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player
from src.characters.monster import Monster

class Play(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()
        self.player = Player(position=Vector2(160, 421))
        self.monster = Monster(position=Vector2(160, 160), follower=self.player)
        self.monster1 = Monster(position=Vector2(400, 400), follower=self.player)
        self.monster2 = Monster(position=Vector2(300, 300), follower=self.player)

        self.entity_group.add(self.player)
        self.entity_group.add(self.monster)
        self.entity_group.add(self.monster1)
        self.entity_group.add(self.monster2)