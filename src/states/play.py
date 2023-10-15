from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player
from src.map.block import Block
from src.map.block import Block1
from src.map.block import Block2
from src.map.block import Block3
from src.map.block import Block4
from src.map.block import Block5
from src.map.block import Block6
from src.map.block import Block7
from src.map.block import Block8
# from src.map.block import Block9
from src.map.block import Block10
from src.map.block import Block11
from src.map.block import Block12
from src.map.block import Block13

class Play(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()

        self.player = Player(position=Vector2(160, 421))
        self.block1 = Block1(position=Vector2(215,543))
        self.block2 = Block2(position=Vector2(0,543))
        self.block = Block(position=Vector2(300,703))
        self.block3 = Block3(position=Vector2(420,680))
        self.block4 = Block4(position=Vector2(352,703))
        self.block5 = Block5(position=Vector2(1136,678))
        self.block6 = Block6(position=Vector2(1016,703))
        self.block7 = Block7(position=Vector2(30,225))
        self.block8 = Block8(position=Vector2(60,225))
        # self.block9 = Block9(position=Vector2(391,237))
        self.block10 = Block10(position=Vector2(1080,240))
        self.block11 = Block11(position=Vector2(920,240))
        self.block12 = Block12(position=Vector2(1173,440))
        self.block13 = Block13(position=Vector2(100,195))



        self.entity_group.add(self.player)
        self.entity_group.add(self.block1)
        self.entity_group.add(self.block2)
        self.entity_group.add(self.block)
        self.entity_group.add(self.block3)
        self.entity_group.add(self.block4)
        self.entity_group.add(self.block5)
        self.entity_group.add(self.block6)
        self.entity_group.add(self.block7)
        self.entity_group.add(self.block8)
        # self.entity_group.add(self.block9)  
        self.entity_group.add(self.block10) 
        self.entity_group.add(self.block11)
        self.entity_group.add(self.block12)
        self.entity_group.add(self.block13)