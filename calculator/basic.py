import math 

# Basic arithemetic operations


def add(x, y):
    try:
        return x + y  
    except TypeError:
        print("Error: please enter numbers, not text")
        return None   
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y        
def divide(x, y):
    try: 
        if y == 0:
            raise ValueError("Cannot divide by zero")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return x / y    
def power(x, y):
    return math.pow(x, y)   
def square_root(x):     
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")    
    return math.sqrt(x)     
def logarithm(x, base=math.e):   
    if x <= 0:
        raise ValueError("Cannot take logarithm of non-positive numbers")    
    return math.log(x, base)
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number")    
    return math.factorial(n)
def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot take modulus by zero")
    return x % y