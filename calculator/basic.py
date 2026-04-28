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
