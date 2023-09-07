from framework.framework import *

class Settings(BaseState):
    def __init__(self):
        super().__init__('settings', 'assets/textures/bg.jpg', WidgetGroup('settings', []))
    
    def update(self, event):
        return super().update(event)
    
    def render(self, display):
        return super().render(display)
    
    def init(self):
        return super().init()