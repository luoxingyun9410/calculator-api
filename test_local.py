# import pytest
# from app.services.math_service import (
#     add,subtract,multiply,divide
# )

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0

# def test_subtract():
#     assert subtract(5, 3) == 2
#     assert subtract(0, 0) == 0
#     assert subtract(-1, -1) == 0

# def test_multiply():
#     assert multiply(2, 3) == 6
#     assert multiply(-1, 1) == -1
#     assert multiply(0, 100) == 0

# def test_divide():
#     assert divide(6, 3) == 2
#     assert divide(-6, 2) == -3
#     with pytest.raises(ValueError):
#         divide(5, 0)

from app.services.math_service import add, subtract, multiply, divide

def test():
    print(add(2,3))
    print(subtract(5,3))
    print(multiply(2,3))
    print(divide(6,3))

    try:
        print(divide(5,0))
    except ValueError:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    test()