from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.states.play import *

class Pause(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)
    
    def __init_state__(self):
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.continueButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 200),
            background=Assets.tt_background_setting_button,
            text=S().continue_button,
            callback= self.continue_game,
            font_size=28,
            scale=1.5
        )

        self.restartButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 300),
            background=Assets.tt_background_setting_button,
            text=S().restart_button,
            callback= self.restart_game,
            font_size=28,
            scale=1.5
        )

        self.menuButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 400),
            background=Assets.tt_background_setting_button,
            text=S().menu_button,
            callback= self.go_menu,
            font_size=28,
            scale=1.5
        )


        self.settingButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 500),
            background=Assets.tt_background_setting_button,
            text=S().setting_button,
            callback= self.push_setting,
            font_size=28,
            scale=1.5
        )
        
        self.widget_group.add(self.continueButton)
        self.widget_group.add(self.restartButton)
        self.widget_group.add(self.menuButton)
        self.widget_group.add(self.settingButton)

    
    def continue_game(self):
        StateMachine.pop()

    def restart_game(self):
        StateMachine.pop()
        StateMachine.__current_state__().__init_state__()

    def go_menu(self):
        StateMachine.pop()
        StateMachine.pop()
    
    def push_setting(self):
        pass