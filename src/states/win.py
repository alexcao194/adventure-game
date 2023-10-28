from framework.framework import *
from framework.core.localization import Localization as S
from src.configs.assets import Assets
from src.states.play import *

class Win(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()

        self.lose_message_1 = Text(
            size=MediaQuery.size,
            position=Vector2(0, 0),
            text=S().lose_message_1
        )

        self.lose_message_2 = Text(
            size=MediaQuery.size,
            position=Vector2(0, 50),
            text=S().lose_message_2
        )

        self.lose_message_3 = Text(
            size=MediaQuery.size,
            position=Vector2(0, 100),
            text=S().lose_message_3,
        )

        self.widget_group.add(self.lose_message_1)
        self.widget_group.add(self.lose_message_2)
        self.widget_group.add(self.lose_message_3)

    def __update__(self, event):

        if event.type == pygame.KEYDOWN:
            StateMachine.pop()
            StateMachine.__current_state__().__init_state__()
            if event.key == pygame.K_ESCAPE:
                StateMachine.pop()
            