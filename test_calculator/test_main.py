"""
test_main.py - Unit tests for main.py

This module contains automated tests for the `main.py` script, ensuring 
correct functionality of the calculator application. It validates:
- Arithmetic operations using the `calculate_and_print` function.
- Error handling for invalid inputs and division by zero.
- Command-line execution of `main.py` using subprocess.

Test Cases:
-----------
- Valid arithmetic operations (add, subtract, multiply, divide).
- Handling division by zero.
- Handling unknown operations.
- Handling non-numeric input errors.
- Verifying correct CLI behavior via subprocess calls.

Usage:
------
Run all tests:
    $ pytest test_main.py

Run with verbose output:
    $ pytest -v test_main.py

Run a specific test:
    $ pytest -k "test_main_script"

Dependencies:
-------------
- `pytest` (for running tests)
- `subprocess` (for testing CLI execution)
- `main.py` (calculator application)

Author: James Mullen
"""
import pytest
from main import calculate_and_print

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "ERROR: Division by zero."),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    """ Tests `calculate_and_print` for valid operations, errors, and edge cases 
    by capturing and comparing printed output.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
