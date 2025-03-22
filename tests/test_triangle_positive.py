import pytest
import math
from src.Triangle import Triangle

@pytest.mark.parametrize("side_a, side_b, side_c, area",
                         [(3,4,5,6),
                          (1.4, 1.3, 1.5, 0.84)],
                         ids=["integer", "float"])
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a=side_a, side_b=side_b, side_c=side_c)
    assert math.fabs(t.area - area) < area/1000, f'площадь должна быть {area}, а она {t.area}'

@pytest.mark.parametrize("side_a, side_b, side_c, perimeter",
                         [(2,3,4,9),
                          (3.1, 3.2, 3.3, 9.6)],
                         ids=["integer", "float"])
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    t=Triangle(side_a=side_a, side_b=side_b, side_c=side_c)
    assert math.fabs(t.perimeter - perimeter) < 0.00001, f'Периметр должен быть {perimeter}, а он {t.perimeter}'