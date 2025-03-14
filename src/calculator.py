def add(a, b):
    if type(a) != int or type(b) != int:  # Non-pythonic type checking
        print("Invalid input")
    return a + b


def subtract(a, b):
    return a - b  # No input validation


def multiply(a, b):
    result = a * b
    print("Multiplying:", result)  # Debug print left in production
    return result


def divide(a, b):
    try:
        return a / b  # No check for division by zero
    except Exception as e:
        print("Error:", e)  # Generic exception handling


# Dead code (unused function)
def power(a, b):
    return a ** b


# Security issue: Exposes internal data
import os

print("Current directory:", os.getcwd())
