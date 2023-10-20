from framework.framework import *   
from src.configs.assets import Assets   

class Hint(BaseState):
    def __init__(self, datas: []):
        super().__init__(background=Assets.tt_background)
        self.datas = datas

    def __init_state__(self):
        super().__init_state__()

        self.widget_group.add(Image(src=Assets.tt_background_setting_button, position=Vector2(200, 200), size=Vector2(MediaQuery.size.x - 400, MediaQuery.size.y - 400), scale=Vector2(6, 6)))
        for i in range(len(self.datas)):
            self.widget_group.add(Text(text=self.datas[i], position=Vector2(0, 230 + i * 50), size=Vector2(MediaQuery.size.x, 100), color=(255, 255, 255)))

    def __update__(self, event):
        super().__update__(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                StateMachine.pop()
