'''
    Framework
    =========
    This is the main framework module. It contains all the classes and functions that are used in the framework.
'''


from framework.utils.vector2 import *
from framework.application import *
from framework.game.state.base_state import *
from framework.game.state.state_machine import *
from framework.core.singleton import *
from framework.core.logger import *
from framework.utils.media_query import *
from framework.game.widget.widget import *
from framework.game.widget.widget_group import *
from framework.game.widget.button import *
from framework.game.entity.entity import *
from framework.game.entity.entity_group import *
from framework.game.animations.animation import *
from framework.game.animations.animation_manager import *
