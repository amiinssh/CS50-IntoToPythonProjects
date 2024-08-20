import unittest
from io import StringIO
import sys
from unittest.mock import patch

from fraction import main

class TestFraction(unittest.TestCase):
    
    def run_test(self, user_input, expected_output):
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value=user_input):
                main()
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_valid_fraction(self):
        self.run_test("1/2", "50%")
        
    def test_zero_numerator(self):
        self.run_test("0/4", "E")
        
    def test_equal_fraction(self):
        self.run_test("3/3", "F")
        
    def test_invalid_fraction_greater_than_one(self):
        self.run_test("5/3", "Invalid input. Please enter a valid fraction.")
        
    def test_invalid_input_non_numeric(self):
        self.run_test("a/b", "Invalid input. Please enter a valid fraction.")
        
    def test_zero_denominator(self):
        self.run_test("1/0", "Invalid input. Please enter a valid fraction.")
        
    def test_fraction_near_zero(self):
        self.run_test("1/100", "E")
        
    def test_fraction_near_one(self):
        self.run_test("99/100", "F")

if __name__ == '__main__':
    unittest.main()
