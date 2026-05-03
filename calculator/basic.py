def add(x, y):
    try:
        return x + y
    except TypeError:
        return None

def subtract(x, y):
    try:
        return x - y
    except TypeError:
        return None

def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return None

def divide(x, y):
    try:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    except (ValueError, TypeError):
        return None