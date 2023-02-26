class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
    def add(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)
    def sub(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)
    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y
    def mag(self):
        return (self.x**2 + self.y**2)**(1/2)
    def magSq(self):
        return (self.x**2 + self.y**2)
    def unit(self):
        return Vector2D(self.x/self.mag(), self.y/self.mag())
    def unit_tangent(self):
        return Vector2D(-self.unit().y, self.unit().x)
    def mult(self, s):
        return Vector2D(s*self.x, s*self.y)