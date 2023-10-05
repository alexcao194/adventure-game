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
        if not isinstance(other, Vector2):
            return False
        return self.x == other.x and self.y == other.y

    def is_negative(self):
        return self.x < 0 or self.y < 0

    def is_positive(self):
        return self.x > 0 or self.y > 0

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    



