from framework.framework import *
from src.states.settings import Settings
from src.character.player import Player

class Menu(BaseState):
    play_button = None
    player = None
    widgets =  WidgetGroup()
    entities = EntityGroup()
    def __init__(self):
        super().__init__('assets/textures/bg.jpg')
    
    def update(self, event):
        super().update(event)
        self.widgets.update(event)
        self.entities.update(event)

    
    def render(self, display):
        super().render(display)
        self.widgets.render(display)
        self.entities.render(display)

    
    def init(self):
        self.player = Player(Vector2(50, 50), Vector2(256, 256))
        self.play_button = ImageButton(Vector2(100, 100), 'assets/textures/play.png', self.open_settings, scale=0.2)
        self.widgets.add(self.play_button)
        self.entities.add(self.player)
        return super().init()
    def open_settings(self):
        StateMachine.push(Settings())

    