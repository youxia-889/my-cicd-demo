import pytest
from calculator import add, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)