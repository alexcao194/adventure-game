from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player
from src.characters.monster import Monster
from src.states.pause import Pause
from src.states.lose import Lose
from src.map.block import *

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
        self.monster_1 = Monster(position=Vector2(200, 300), follower=self.player)
        self.monster_2 = Monster(position=Vector2(500, 300), follower=self.player)
        self.monster_3 = Monster(position=Vector2(800, 300), follower=self.player)
        self.monster_4 = Monster(position=Vector2(1100, 300), follower=self.player)


        self.entity_group.add(self.monster_1)
        self.entity_group.add(self.monster_2)
        self.entity_group.add(self.monster_3)
        self.entity_group.add(self.monster_4)
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
    

    def __update__(self, event):
        super().__update__(event=event)

        if(self.player.hp <= 0):
            StateMachine.push(Lose())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                StateMachine.push(Pause())
                