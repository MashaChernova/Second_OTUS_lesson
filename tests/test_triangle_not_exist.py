import pytest
from src.Triangle import Triangle


@pytest.mark.xfail(raises = ValueError)
def test_circle_area(side_a=1,side_b=2, side_c=4):
    Triangle(11,2,5)

