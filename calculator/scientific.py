import math

def power(x, y):
    try:
        return x ** y
    except TypeError:
        return None

def sqrt(x):
    try:
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(x)
    except (ValueError, TypeError):
        return None

def log(x, base=math.e):
    try:
        if x <= 0:
            raise ValueError("Logarithm only works with positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Invalid base")
        return math.log(x, base)
    except (ValueError, TypeError):
        return None

def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial only works with positive numbers")
        if not isinstance(n, int):
            raise ValueError("Factorial only works with whole numbers")
        return math.factorial(n)
    except (ValueError, TypeError):
        return None

def sin(x):
    try:
        return math.sin(math.radians(x))
    except TypeError:
        return None

def cos(x):
    try:
        return math.cos(math.radians(x))
    except TypeError:
        return None

def tan(x):
    try:
        if x % 180 == 90:
            raise ValueError("Tangent is undefined for this angle")
        return math.tan(math.radians(x))
    except (ValueError, TypeError):
        return None

def cot(x):
    try:
        if x % 180 == 0:
            raise ValueError("Cotangent is undefined for this angle")
        return 1 / math.tan(math.radians(x))
    except (ValueError, TypeError):
        return None

def modulus(x, y):
    try:
        if y == 0:
            raise ValueError("Cannot take modulus by zero")
        return x % y
    except (ValueError, TypeError):
        return None

def exp(x):
    try:
        return math.exp(x)
    except TypeError:
        return None