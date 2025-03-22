import pytest

from src.Circle import Circle

@pytest.mark.parametrize("radius, area",
                         [(1,3.1415),
                          (0.5,0.25*3.1415)],
                         ids=["integer", "float"])
def test_circle_area(radius, area):
    c = Circle(radius=radius)
    assert c.area == area, f'площадь должна быть {area}, а она {c.area}'

@pytest.mark.parametrize("radius, perimeter",
                         [(1,6.283),
                          (0.5, 3.1415)],
                         ids=["integer", "float"])
def test_circke_perimeter(radius, perimeter):
    с = Circle(radius=radius)
    assert с.perimeter == perimeter, f'Периметр должен быть 12, а он {с.perimeter}'