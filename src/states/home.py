from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.states.setting import Setting
from src.states.play import Play

class Home(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)
    
    def __init_state__(self):
        super().__init_state__()
        screenWidth = MediaQuery.size.x
        screenHeight = MediaQuery.size.y
        
        self.continueButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 200),
            background=Assets.tt_background_setting_button,
            text=S().start_button,
            callback= self.start_game,
            font_size=28,
            scale=1.5
        )

        self.restartButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 300),
            background=Assets.tt_background_setting_button,
            text=S().continue_button,
            callback= self.continue_game,
            font_size=28,
            scale=1.5
        )

        self.menuButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 400),
            background=Assets.tt_background_setting_button,
            text=S().setting_button,
            callback= self.open_setting,
            font_size=28,
            scale=1.5
        )


        self.settingButton = ImageButton(
            position=Vector2(screenWidth//2 - 120, 500),
            background=Assets.tt_background_setting_button,
            text=S().about_button,
            callback= self.open_about,
            font_size=28,
            scale=1.5
        )

        self.widget_group.add(self.continueButton)
        self.widget_group.add(self.restartButton)
        self.widget_group.add(self.menuButton)
        self.widget_group.add(self.settingButton)

    
    def start_game(self):
        StateMachine.push(Play())     
        pass

    def continue_game(self):
        StateMachine.push(Play())
        pass
    
    def open_setting(self):
        StateMachine.push(Setting())
    
    def open_about(self):
        # StateMachine().push(About())
        pass