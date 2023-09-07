from framework.core.singleton import Singleton
from framework.utils.vector2 import Vector2

'''
MediaQuery is a singleton class that contains the size of the window and the aspect ratio.
'''
class MediaQuery(Singleton):
    size = Vector2(1200, 800)
    aspect_ratio = size.x / size.y
    