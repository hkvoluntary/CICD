def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed!")

