from framework.framework import *
from src.states.menu import Menu
import pygame


pygame.init()
app = Application(MediaQuery.size, Menu())
app.run()

