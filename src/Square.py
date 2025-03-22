from Rectangle import Rectangle
from Sides import Sides

class Squere (Rectangle):
    def __init__(self, side_a):
          super().__init__(side_a, side_a)