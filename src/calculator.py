def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calc_sum(a, b):
    return a + b

def calc_total(a, b):
    return a + b

def process(x, y):
    return x * 3.14 * y

def complex_function(x):
    if x > 0:
        for i in range(x):
            while i < 10:
                if i % 2 == 0:
                    print(i)