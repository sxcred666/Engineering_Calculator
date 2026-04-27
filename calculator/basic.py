import math 

# Basic arithemetic operations

#functions for basic arithmetic operations: addition, subtraction, multiplication, division, power, square root, logarithm, factorial, and modulus. Each function includes error handling to manage invalid inputs and edge cases.
def add(x, y):
    try:
        return x + y  # add(2, 3) = 5, but not 5.0
    except TypeError:
        print("Error: please enter numbers, not text")
        return None   
def subtract(x, y):
    try:
        return x - y   # subtract(5, 2) = 3, but not 3.0 
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
def multiply(x, y):
    try:
        return x * y    # multiply(2, 3) = 6, but not 6.0    
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
def divide(x, y):
    try: 
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    except ValueError as e:  # Handle division by zero error
        print(f"Error: {e}")
        return None          
    except TypeError:  # Handle non-numeric input error
        print("Error: please enter numbers, not text")
        return None
def power(x, y):
    try:
        return x ** y
    except TypeError:   # 2 ** 3 = 8, but not 8.0
        print("Error: please enter numbers, not text")
        return None
def square_root(x):    
    try: 
        if x < 0:  # check for negative input
            raise ValueError("Cannot take square root of a negative number")    
        return math.sqrt(x)     # math.sqrt(4) = 2.0, but not 2
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
def logarithm(x, base=math.e):   #base is optional, default is natural logarithm
    try:
        if x <= 0:
            raise ValueError("Logarithm only works with positive numbers")    
        if base <=0 or base == 1: # base must be positive and not equal to 1
            raise ValueError("Base must be a positive number and not equal to 1")
        return math.log(x, base)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError: 
        print("Error: please enter numbers, not text")
        return None 
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial only works with non-negative integers")
        if not isinstance(n, int): # check if n is an integer
            raise ValueError("Factorial only works with integers")
        return math.factorial(n)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
def modulus(x, y):
    try:
        if y == 0:
            raise ValueError("Cannot take modulus by zero")
        return x % y
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: please enter numbers, not text")
        return None