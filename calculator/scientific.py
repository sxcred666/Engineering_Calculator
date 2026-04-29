import math 

# Scientific calculator functions

def power(x,y):
    try:
        return x ** y
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
    
def sqrt(x):
    try:
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(x)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def log(x, base=math.e):    
    try:
        if x <= 0:
            raise ValueError("Cannot take logarithm of non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1")
        return math.log(x, base)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Cannot take factorial of a negative number")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        return math.factorial(n)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def sin(x):
    try:
        return math.sin(math.radians(x))
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
    
def cos(x):
    try:
        return math.cos(math.radians(x))
    except TypeError:
        print("Error: please enter numbers, not text")
        return None
    
def tan(x):
    try:
        if x % 180 == 90:
            raise ValueError("Tangent is undefined for this angle")
        return math.tan(math.radians(x))
    except ValueError as e:
        print(f"Error: {e}")
        return None 
    
def cot(x):
    try:
        if x % 180 == 0:
            raise ValueError("Cotangent is undefined for this angle")
        return 1 / math.tan(math.radians(x))
    except ValueError as e:
        print(f"Error: {e}")
        return None

def modulus(x, y):
    try:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x % y
    except ValueError as e:
        print(f"Error: {e}")
        return None

def exp(x):
    try:
        return math.exp(x)
    except TypeError:
        print("Error: please enter numbers, not text")
        return None