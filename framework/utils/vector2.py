import math

class Vector2():
    '''
    Vector2 class
    x: float - the x coordinate
    y: float - the y coordinate
    '''
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x, self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
def distance(a : Vector2, b : Vector2):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)



