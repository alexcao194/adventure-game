![Tree](https://media.discordapp.net/attachments/960780341952544798/1160196744311754832/image.png?ex=6533c86b&is=6521536b&hm=60b8953f65b51e27dbdb03c23e9ff012b1bfe4d440dc3f153b4ece23bd871799&=&width=211&height=671)

**player.py**
```python
from framework.framework import *
from src.configs.assets import Assets

class Player(Entity):
    def __init__(self, position: Vector2 = None, hitbox: Vector2 = None):
        super().__init__(hitbox=hitbox, position=position)
        self.speed = 3

        self.animation_manager = AnimationManager(
            action_animation = {
                'death': ActionAnimation(
                    src=Assets.ani_death,
                    frame_count=10,
                    entity=self,
                    delay=2
                )
            },
            repeat_animation = {
                'death': RepeatAnimation(
                    src=Assets.ani_death,
                    frame_count=10,
                    entity=self,
                    delay=2
                ),
                'idle': RepeatAnimation(
                    src=Assets.ani_idle,
                    frame_count=6,
                    entity=self,
                    delay=2
                ),
            },
            current_animation="idle"
        )

    def __update__(self, event):
        super().__update__(event)
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            self.position.x -= self.speed
            self.fliped = True
            self.animation_manager.current_animation = "idle"
        elif(keys[pygame.K_RIGHT]):
            self.position.x += self.speed
            self.fliped = False
            self.animation_manager.current_animation  = "idle"
        elif(keys[pygame.K_UP]):
            self.position.y -= self.speed
            self.animation_manager.current_animation = "idle"
        elif(keys[pygame.K_DOWN]):
            self.position.y += self.speed
            self.animation_manager.current_animation = "idle"
        else:
            self.animation_manager.current_animation = "idle"

        if(keys[pygame.K_SPACE]):
            self.animation_manager.change_animation("death")
        else:
            self.animation_manager.change_animation("idle")

        if(keys[pygame.K_v]):
            self.animation_manager.play_action("death")
```

**block.py** (this is a simple block that can be used as a background)
```python
from framework.framework import *

class Block(Entity):
    def __init__(self, position: Vector2, hitbox: Vector2 = None, texture: str = None):
        super().__init__(position=position, hitbox=hitbox)
        self.texture = Texture(texture=texture, entity=self)
```

**assets.py**
```python
from framework.framework import *

class Assets(Singleton):
    tt_demo = 'assets/demo.jpg' # remember to use relative path, standard format is 'assets/<filename>'
    ani_death = 'assets/death/' # remember to use relative path, standard format is 'assets/<folder>'
    ani_idle = 'assets/idle/'
```

**menu.py**
```python
from framework.framework import *
from framework.framework import Localization as S
from src.configs.assets import Assets
from src.character.player import Player
from src.map.block import Block
from src.states.settings import Settings

class Menu(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_demo)
    
    def __init_state__(self):
        super().__init_state__()

        self.button = Button(
            position=Vector2(100, 100),
            size=Vector2(300, 300),
            callback=self.change_language,
            text=S().change_language,
            font_size=50
        )

        self.image_button = ImageButton(
            position=Vector2(500, 100),
            background=Assets.tt_demo,
            callback=self.on_click,
            scale=0.5
        )

        self.image_button_with_text = ImageButton(
            position=Vector2(500, 500),
            background=Assets.tt_demo,
            callback=self.pop,
            scale=0.5,
            text=S().contact,
            font_size=50
        )

        self.text = Text(
            position=Vector2(100, 500),
            size=Vector2(300, 300),
            text=S().menu,
            font_size=50
        )

        self.image = Image(
            position=Vector2(500, 500),
            src=Assets.tt_demo,
            scale=Vector2(1, 0.5)
        )

        self.player = Player(
            position=Vector2(400, 400),
            hitbox=Vector2(256, 256)
        )

        self.block = Block(
            position=Vector2(500, 500),
            hitbox=Vector2(100, 100),
            texture=Assets.tt_demo
        )

        self.widget_group.add(self.button)
        self.widget_group.add(self.image_button)
        self.widget_group.add(self.text)
        self.widget_group.add(self.image)
        self.widget_group.add(self.block)
        self.widget_group.add(self.player)
        self.widget_group.add(self.image_button_with_text)

    def on_click(self):
        StateMachine.push(Settings())
    
    def change_language(self):
        S.language = 'vi'
        print(S().menu)
        print(S().language)
    
    def pop(self):
        StateMachine.pop()
```

And that's it! You can run the game by running `python main.py` in the root directory. 
We will see this **shit**:
![DemoScreen](https://cdn.discordapp.com/attachments/960780341952544798/1159540448403148890/image.png?ex=65316532&is=651ef032&hm=a61c72505360f37d07ec4695459a537165ed0a81ae7e02c4d8e588cf44234750&)