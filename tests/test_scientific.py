import os, sys, math

import pytest # for manipulating file paths and system-specific parameters
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # add the parent directory to the system path to allow importing modules from the calculator package

from calculator.scientific import power, sqrt, log, sin, cos, tan, exp, factorial, modulus, cot # import the scientific functions from the calculator package

def test_sqrt():
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    assert sqrt(-1) is None # Negative input should return None

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) is None # Negative input should return None
    assert factorial(3.5) is None # Non-integer input should return None

def test_sin():
    assert sin(0) == 0.0
    assert sin(90) == pytest.approx(1.0)
    assert sin(-90) == pytest.approx(-1.0)

def test_cos():
    assert cos(0) == pytest.approx(1.0)
    assert cos(90) == pytest.approx(0.0, abs=1e-9)
    assert cos(180) == pytest.approx(-1.0)

def test_tan():
    assert tan(0) == pytest.approx(0.0)
    assert tan(90) is None # Input of 90 degrees should return None
    assert tan(45) == pytest.approx(1.0)

def test_cot():
    assert cot (90) == pytest.approx(0.0, abs=1e-9) 
    assert cot(45) == pytest.approx(1.0)
    assert cot(0) is None # Input of 0 degrees should return None
    assert cot(180) is None # Input of 180 degrees should return None
 
def test_power():
    assert power (2, 3) == 8
    assert power(2, 0) == 1
    assert power(-2, 2) == 4

def test_log():
    assert log(1) == pytest.approx(0.0)
    assert log(0) is None # Logarithm of zero should return None
    assert log(-1) is None # Logarithm of negative number should return None
    assert log(100, 10) == pytest.approx(2.0)   

def test_modulus():
    assert modulus(10, 3) == 1 # Modulus of 10 by 3 should be 1
    assert modulus(10, 0) is None # Modulus by zero should return None 
    assert modulus(0, 5) == 0 # Modulus of zero by any number should be zero

def test_exp():
    assert exp(0) == pytest.approx(1.0) # Exponential of 0 should be 1
    assert exp(1) == pytest.approx(math.e) # Exponential of 1 should be approximately e
    assert exp(-1) == pytest.approx(1 / math.e) # Exponential of negative number should be approximately 1/e