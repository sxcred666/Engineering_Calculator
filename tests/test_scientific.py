import os, sys # for manipulating file paths and system-specific parameters
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # add the parent directory to the system path to allow importing modules from the calculator package

def test_scientific():
    from calculator.scientific import sin, cos, tan, log, exp # import the scientific functions from the calculator package

    assert round(sin(0), 5) == 0 
    assert round(cos(0), 5) == 1
    assert round(tan(0), 5) == 0
    assert round(log(1), 5) == 0
    assert round(exp(1), 5) == 2.71828
    