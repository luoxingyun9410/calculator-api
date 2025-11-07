import pytest
from app.services.math_service import(
    add, subtract, multiply, divide
)

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1.5) == 0.5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(4, 2) == 8
    assert multiply(-1, 3) == -3

def test_divide():
    assert divide(6, 2) == 3
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)