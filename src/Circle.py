from Figure import Figure
from Sides import Sides

class Circle(Figure) :
    def __init__(self, radius):
        self.radius = Sides(radius).isCorrectSide

    @property
    def perimeter(self):
        return 2 * 3.1415 * self.radius

    @property
    def area(self):
        return (3.1415 * self.radius * self.radius)

