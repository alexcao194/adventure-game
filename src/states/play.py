from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player
from src.characters.monster import Monster
from src.map.block import *

class Play(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()


        #Objects
        self.player = Player(position=Vector2(160,421))
        self.block1 = Block(texture=Assets.tt_block_1,hitbox=Vector2(40,100), size=Vector2(53,43), offset=Vector2(0,30),position=Vector2(215,543))
        self.block2 = Block(texture=Assets.tt_block_2,hitbox=Vector2(300,300), size=Vector2(0,1), offset=Vector2(0,23),position=Vector2(0,543))
        self.block3 = Block(texture=Assets.tt_block_3,hitbox=Vector2(0,1), size=Vector2(80,175), offset=Vector2(0,50),position=Vector2(420,680))
        self.block4 = Block(texture=Assets.tt_block_4,hitbox=Vector2(50,20), size=Vector2(100,100), offset=Vector2(0,50),position=Vector2(352,703))
        self.block5 = Block(texture=Assets.tt_block_3,hitbox=Vector2(80,10), size=Vector2(80,189), offset=Vector2(0,50),position=Vector2(1136,678))
        self.block6 = Block(texture=Assets.tt_block_2,hitbox=Vector2(298,300), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(1016,703))
        self.block7 = Block(texture=Assets.tt_block_2,hitbox=Vector2(50,320), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(30,225))
        self.block8 = Block(texture=Assets.tt_block_2,hitbox=Vector2(400,12), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(60,225))
        #self.block9 = Block(texture=Assets.tt_block_1,hitbox=Vector2(40,100), size=Vector2(53,43), offset=Vector2(0,30),position=(215,543))
        self.block10 = Block(texture=Assets.tt_block_2,hitbox=Vector2(150,250), size=Vector2(0,1), offset=Vector2(0,0),position=Vector2(1080,240))
        self.block11 = Block(texture=Assets.tt_block_2,hitbox=Vector2(170,10), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(920,240))
        self.block12 = Block(texture=Assets.tt_block_2,hitbox=Vector2(40,95), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(1173,440))
        self.block13 = Block(texture=Assets.tt_block_2,hitbox=Vector2(43,100), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(100,195))
        self.block14 = Block(texture=Assets.tt_block_2,hitbox=Vector2(550,100), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(300,703))



        self.tree1 = Block(texture=Assets.tt_plant_1,hitbox=Vector2(25,25),size=Vector2(230,350),offset=Vector2(100,325),position=Vector2(165,22))
        self.tree2 = Block(texture=Assets.tt_plant_0,hitbox=Vector2(25,25),size=Vector2(270,360),offset = Vector2(122,340), position=Vector2(915,190))

        self.stone1 = Block(texture=Assets.tt_stone_9,hitbox=Vector2(150,75),size=Vector2(150,120),offset=Vector2(0,45),position=Vector2(490,570))
        self.stone2 = Block(texture=Assets.tt_headstone_6,hitbox=Vector2(75,75),size=Vector2(80,115),offset=Vector2(0,45),position=Vector2(432,350))
        self.stone3 = Block(texture=Assets.tt_stone_2,hitbox=Vector2(75,45),size=Vector2(75,45),offset=Vector2(0,0),position=Vector2(685,601))
        self.stone4 = Block(texture=Assets.tt_stone_1,hitbox=Vector2(45,40),size=Vector2(45,40),offset=Vector2(0,0),position=Vector2(805,661))
        self.stone5 = Block(texture=Assets.tt_stone_3,hitbox=Vector2(65,50),size=Vector2(65,50),offset=Vector2(0,0),position=Vector2(975,601))

        self.bin1 = Block(texture=Assets.tt_bin_2,hitbox=Vector2(55,33),size=Vector2(58,88),offset=Vector2(0,55),position=Vector2(950,459))
        self.bin2 = Block(texture=Assets.tt_bin_1,hitbox=Vector2(58,65),size=Vector2(58,65),offset=Vector2(0,0),position=Vector2(850,370))


        self.wall1 = Block(texture=Assets.tt_block_2,hitbox=Vector2(160,155),size=Vector2(160,155),offset=Vector2(0,0),position=Vector2(460,253))
        self.wall2 = Block(texture=Assets.tt_block_2,hitbox=Vector2(160,155),size=Vector2(160,155),offset=Vector2(0,0),position=Vector2(770,253))


        self.wall3 = Block(texture=Assets.tt_block_2,hitbox=Vector2(13,227),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(620,253))
        self.wall4 = Block(texture=Assets.tt_block_2,hitbox=Vector2(13,227),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(757,253))

        self.entity_group.add(self.monster_1)
        self.entity_group.add(self.monster_2)
        self.entity_group.add(self.monster_3)
        self.entity_group.add(self.monster_4)
        self.entity_group.add(self.player)
        self.entity_group.add(self.wall1)
        self.entity_group.add(self.block1)
        self.entity_group.add(self.block2)
        self.entity_group.add(self.block14)
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
        self.entity_group.add(self.tree1)
        self.entity_group.add(self.tree2)
        self.entity_group.add(self.stone1)
        self.entity_group.add(self.stone2)
        self.entity_group.add(self.stone3)
        self.entity_group.add(self.stone4)
        self.entity_group.add(self.stone5)
        self.entity_group.add(self.bin1)
        self.entity_group.add(self.bin2)
        self.entity_group.add(self.wall1)
        self.entity_group.add(self.wall2)
        self.entity_group.add(self.wall3)
        self.entity_group.add(self.wall4)
