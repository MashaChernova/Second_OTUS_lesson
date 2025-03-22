import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle

@pytest.mark.xfail(raises = ValueError)
def test_add_area_negativ():
    figure1 = Rectangle(2, 4)
    figure2 = 8
    figure1.add_area(figure2)