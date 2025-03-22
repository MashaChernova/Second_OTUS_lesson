import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle

@pytest.mark.parametrize("figure1, figure2",
                         [(Square(1),Rectangle(1,2)),
                          (Triangle(3,4,5), Triangle(0.5,1.2,1.3)),
                          (Circle(1.0),Square(2.0)),
                          (Rectangle(1,2),Square(3))],
                         ids=["Squere_Rectangle", "Triangle_Triangle", "Circle_Squere", "Rectangle_Squere"])
def test_circle_area(figure1, figure2):
    assert figure1.add_area(figure2) == figure1.area + figure2.area, f'площадь не равна сумме площадей'