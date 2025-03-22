from Figure import Figure
import math
from Sides import Sides

class Triangle(Figure) :
    def __init__(self, side_a,side_b, side_c):
        self.side_a = Sides(side_a).isCorrectSide
        self.side_b = Sides(side_b).isCorrectSide
        self.side_c = Sides(side_c).isCorrectSide
        if max(self.side_a, self.side_b, self.side_c) > (self.side_a + self.side_b + self.side_c) / 2:
            raise ValueError("Треугольник не существует")
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        semiperimetr = self.perimeter/2
        return math.sqrt((semiperimetr-self.side_b)*(semiperimetr-self.side_b)*(semiperimetr-self.side_c)*semiperimetr)
