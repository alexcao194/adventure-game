from framework.framework import *
from src.configs.assets import Assets

class Monster(Entity):
    def __init__(self, position: Vector2, follower: Entity):
        super().__init__(hitbox=Vector2(32, 32), position=position, size=Vector2(96, 66), offset=Vector2(32, 22))
        self.show_hitbox = False
        self.follower = follower
        self.init_position = position
        self.following = False
        self.active_range = 200
        self.animation_manager = AnimationManager(
            action_animation={
                "attack": ActionAnimation(src=Assets.ani_monster_attack_arround, frame_count=9, delay=150, entity=self),
                "die": ActionAnimation(src=Assets.ani_monster_die, frame_count=6, delay=150, entity=self),
            },
            repeat_animation={
                "idle": RepeatAnimation(src=Assets.ani_monster_idle, frame_count=6, delay=150, entity=self),
                "run": RepeatAnimation(src=Assets.ani_monster_run, frame_count=12, delay=150, entity=self),
            },
            current_animation="idle"
        )
    
    def __update__(self, event):
        super().__update__(event=event)
        if(self.position == self.init_position):
            self.animation_manager.change_animation("idle")
        
        if(self.follower.position.distance(self.init_position) < self.active_range):
            self.following = True
        else:
            self.following = False
        
        if(self.following == False and self.position != self.init_position):
            self.animation_manager.change_animation("run")
            movement = self.init_position - self.position
            self.set_position(self.position + (movement * Clock.delta_time) * 0.8)
            if(self.position.distance(self.init_position) < 5):
                self.set_position(self.init_position)
                self.animation_manager.change_animation("idle")
        
        if(self.following):
            self.animation_manager.change_animation("run")
            movement = self.follower.position - self.position
            self.set_position(self.position + (movement * Clock.delta_time) * 0.8)
            for collision in self.collisions:
                if(collision.__class__.__name__ == 'Player'):
                    self.animation_manager.play_action("attack")
                    break



        