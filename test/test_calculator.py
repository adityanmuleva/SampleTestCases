import unittest
from app.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    # Positive Test Cases
    def test_add_positive(self):
        self.assertEqual(add(5, 3), 8)  # Normal addition
        self.assertEqual(add(-1, 1), 0) # Negative and positive number

    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)  # Normal subtraction
        self.assertEqual(subtract(0, 0), 0)   # Zero subtraction

    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 7), 21)  # Positive numbers
        self.assertEqual(multiply(-2, 5), -10) # Negative and positive

    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)   # Normal division
        self.assertAlmostEqual(divide(7, 3), 2.3333, places=4) # Float result

    # Negative Test Cases
    def test_add_negative(self):
        self.assertNotEqual(add(5, 3), 10)  # Incorrect result
        self.assertNotEqual(add(-5, -5), 0) # Incorrect result

    def test_subtract_negative(self):
        self.assertNotEqual(subtract(10, 4), 3) # Incorrect result
        self.assertNotEqual(subtract(5, 10), 0) # Incorrect result

    def test_multiply_negative(self):
        self.assertNotEqual(multiply(3, 7), 25) # Incorrect result
        self.assertNotEqual(multiply(0, 5), 5)  # Incorrect result

    def test_divide_negative(self):
        with self.assertRaises(ValueError):     # Division by zero
            divide(10, 0)

        self.assertNotEqual(divide(10, 2), 6)  # Incorrect result
    
    # Edge Cases
    def test_edge_cases(self):
        self.assertEqual(add(0, 0), 0)           # Zero edge case
        self.assertEqual(subtract(1, 1), 0)      # Identity property
        self.assertEqual(multiply(1, 0), 0)      # Multiplication by zero
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4) # Small division

if __name__ == '__main__':
    unittest.main()
