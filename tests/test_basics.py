import sys, pytest
sys.path.insert(0, '/home/ksingh/python_learning')
from calculator import add, subtract, multiply, divide
###
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_subtract_negative_result():
    assert subtract(3, 10) == -7

def test_divide():
      assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)