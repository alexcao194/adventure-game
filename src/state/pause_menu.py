@@ -1,61 +0,0 @@
from framework.framework import *
from framework.framework import Localization as S
from src.configs.assets import Assets

class MenuPause(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)
    
    def __init_state__(self):
        super().__init_state__()

        self.image_button_with_text_continue = ImageButton(
            background=Assets.tt_2,
            callback=self.__on_resume__,
            position=Vector2(550,200),
            scale=1,
            text='Continue',
            font_size=70
        )

        self.image_button_with_text_restart = ImageButton(
            background=Assets.tt_2,
            callback=self.__on_exit__,
            position=Vector2(550,300),
            scale=1,
            text='Restart',
            font_size=70
        )

        self.image_button_with_text_setting = ImageButton(
            background=Assets.tt_2,
            callback=self.on_click,
            position=Vector2(550,400),
            scale=1,
            text='Setting',
            font_size=70
        )

        self.image_button = ImageButton(
            position=Vector2(1990, 10),
            background=Assets.tt_demo,
            callback=self.on_click,
            scale=0.5
        )

        self.widget_group.add(self.image_button_with_text_continue)
        self.widget_group.add(self.image_button_with_text_restart)
        self.widget_group.add(self.image_button_with_text_setting)
        self.widget_group.add(self.image_button)

    def on_click(self):
        pass

    def pop(self):
        pass