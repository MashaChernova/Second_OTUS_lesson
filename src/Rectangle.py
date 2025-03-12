from Figure import Figure
from Sides import Sides

class Rectangle(Figure) :
    def __init__(self, side_a,side_b):
        self.side_a = Sides(side_a).isCorrectSide
        self.side_b = Sides(side_b).isCorrectSide

    @property
    def perimeter(self):
        return (self.side_a + self.side_b)*2

    @property
    def area(self):
        return (self.side_a * self.side_b)