import pytest
import math

from src.Rectangle import Rectangle

@pytest.mark.parametrize("side_a, side_b, area",
                         [(3,4,12),
                          (0.9, 1.1, 0.99)],
                         ids=["integer", "float"])
def test_triangle_area(side_a, side_b, area):
    r = Rectangle(side_a=side_a, side_b=side_b)
    assert math.fabs(r.area - area) < 0.000001, f'площадь должна быть {area}, а она {r.area}'

@pytest.mark.parametrize("side_a, side_b, perimeter",
                         [(2,3,10),
                          (3.1, 3.2, 12.6)],
                         ids=["integer", "float"])
def test_triangle_perimeter(side_a, side_b, perimeter):
    r=Rectangle(side_a=side_a, side_b=side_b)
    assert math.fabs(r.perimeter - perimeter) < 0.00001, f'Периметр должен быть {perimeter}, а он {r.perimeter}'