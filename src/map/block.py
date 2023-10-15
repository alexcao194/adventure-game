from framework.framework import*
from framework.utils.vector2 import Vector2
from src.configs.assets import Assets


class Block(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(550,100), position=position, size=Vector2(0,1), offset=Vector2(0,25))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)


class Block1(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(40,100), position=position, size=Vector2(53,43), offset=Vector2(0,30))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_1, entity=self)


class Block2(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(300,300), position=position, size=Vector2(0,1), offset=Vector2(0,23))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)


class Block3(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(0,1), position=position, size=Vector2(80,175), offset=Vector2(0,50))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_3, entity=self)



class Block4(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(50,20), position=position, size=Vector2(100,100), offset=Vector2(0,50))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_4, entity=self)


class Block5(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(80,10), position=position, size=Vector2(80,189), offset=Vector2(0,50))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_3, entity=self)

class Block6(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(298,300), position=position, size=Vector2(0,1), offset=Vector2(0,25))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)

class Block7(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(50,320), position=position, size=Vector2(0,1), offset=Vector2(0,25))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)


class Block8(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(400,12), position=position, size=Vector2(0,1), offset=Vector2(0,25))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)


# class Block9(Entity):
#     def __init__(self, position: Vector2):
#         super().__init__(hitbox=Vector2(1,1), position=position, size=Vector2(70,83), offset=Vector2(0,0))
#         self.show_hitbox=True;
#         self.texture = Texture(texture=Assets.tt_block_5, entity=self)

class Block10(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(150,250), position=position, size=Vector2(0,1), offset=Vector2(0,0))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)

class Block11(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(170,10), position=position, size=Vector2(0,1), offset=Vector2(0,10))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)

class Block12(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(40,95), position=position, size=Vector2(0,1), offset=Vector2(0,10))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)

class Block13(Entity):
    def __init__(self, position: Vector2):
        super().__init__(hitbox=Vector2(43,100), position=position, size=Vector2(0,1), offset=Vector2(0,10))
        self.show_hitbox=True;
        self.texture = Texture(texture=Assets.tt_block_2, entity=self)