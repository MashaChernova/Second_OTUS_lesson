import pytest

from src.Square import Square

@pytest.mark.parametrize("side_a, area",
                         [(4,16),
                          (0.5,0.25)],
                         ids=["integer", "float"])
def test_area(side_a, area):
    s = Square(side_a=side_a)
    assert s.area == area, f'площадь должна быть {area}, а она {s.area}'

@pytest.mark.parametrize("side_a, perimeter",
                         [(3,12),
                          (5.3, 21.2)],
                         ids=["integer", "float"])
def test_perimeter(side_a, perimeter):
    s = Square(side_a=side_a)
    assert s.perimeter == perimeter, f'Периметр должен быть 12, а он {s.perimeter}'