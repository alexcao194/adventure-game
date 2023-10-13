from framework.framework import *
from src.states.setting import Setting

app = Application()
app.init_state(Setting())
app.run()
