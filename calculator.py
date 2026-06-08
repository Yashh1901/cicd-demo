# calculator.py

def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    this is not valid python ← add this line

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b