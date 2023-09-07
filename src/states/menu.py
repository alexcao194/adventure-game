from framework.framework import *
from src.states.settings import Settings
from src.character.player import Player

class Menu(BaseState):
    play_button = None
    player = None
    def __init__(self):
        super().__init__('menu', 'assets/textures/bg.jpg', WidgetGroup('menu', []))
    
    def update(self, event):
        return super().update(event)
    
    def render(self, display):
        super().render(display)
        self.player.render(display)

    
    def init(self):
        self.player = Player('player', Vector2(200, 200), Vector2(32, 32))
        self.play_button = ImageButton('play', Vector2(100, 100), 'assets/textures/play.png', self.open_settings, scale=0.2)
        self.widgets.add(self.play_button)
        return super().init()
    def open_settings(self):
        StateMachine.push(Settings())

    