from framework.core.singleton import Singleton
from framework.utils.vector2 import Vector2
class MediaQuery(Singleton):
    size = Vector2(1200, 800)
    aspect_ratio = size.x / size.y
    