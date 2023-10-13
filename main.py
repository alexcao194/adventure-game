from framework.framework import *
from src.states.menu import Menu


app = Application()
app.init_state(Menu())
app.run()
