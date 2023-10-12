from framework.framework import *
from src.state.pause_menu import MenuPause


app = Application()
app.init_state( MenuPause())
app.run()
