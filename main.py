from framework.framework import *
from src.states.menu import Menu

app = Application(MediaQuery.size, Menu())
app.run()

