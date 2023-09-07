import math

class Vector2():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x, self.y)
    
def distance(a : Vector2, b : Vector2):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
