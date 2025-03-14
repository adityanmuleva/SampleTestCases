# Code Smells Examples for SonarQube Detection

# 1. Complexity Smells

def complex_function(x):
    if x > 0:
        for i in range(x):
            while i < 10:
                if i % 2 == 0:
                    print(i)

# 2. Duplication Smells

def calc_sum(a, b):
    return a + b

def calc_total(a, b):
    return a + b  # Duplicate logic

# 3. Bad Naming Smells

def process(x, y):
    return x * 3.14 * y  # Magic number (3.14)

# 4. Code Structure Smells

class Order:
    def __init__(self, price):
        self.price = price

class Invoice:
    def get_order_price(self, order):
        return order.price  # Directly accessing private data

# 5. Exception Handling Smells

def risky_operation():
    raise ValueError("Error occurred")

try:
    risky_operation()
except Exception:  # Generic exception
    pass  # Swallowing the error

# 6. Performance Smells

data = [i for i in range(1000000)]
for i in range(len(data)):  # Inefficient loop
    print(data[i])

# 7. Code Style Smells

def unused_function():
    pass  # Dead code, never called

# 8. Security Smells

password = "admin123"  # Hardcoded password

def get_user_query(username):
    return f"SELECT * FROM users WHERE name='{username}'"  # SQL Injection risk

# 9. Testability Smells

GLOBAL_VAR = 42  # Global state impairs testability

def use_global():
    return GLOBAL_VAR

# 10. Documentation Smells

def calculate_area(r):
    # This calculates the circumference (incorrect comment)
    return 3.14 * r * r
