from calc import square, cube
import pytest

def test_square():
    # pytest.raises()
    n = 2
    assert square(n) == 4


def test_cube():
    n = 2
    assert cube(n) == 8