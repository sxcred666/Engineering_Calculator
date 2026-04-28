import sys, os # for manipulating file paths and system-specific parameters
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # add the parent directory to the system path to allow importing modules from the calculator package

from calculator.basic import add, subtract, multiply, divide # import the basic arithmetic functions from the calculator package

def test_add():
    assert add(2, 3) == 5 
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, -5) == 5
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
