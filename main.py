"""
Entry point for the calculator application.

This script takes three command-line arguments:
1. First number (numeric value)
2. Second number (numeric value)
3. Operation (add, subtract, multiply, divide)

Example usage:
    $ python main.py 10 5 add
    The result of 10 add 5 is equal to 15

Handles invalid inputs and division by zero gracefully.

Author: James Mullen
"""

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

#pylint: disable=unnecessary-dunder-call, invalid-name
# pylint: disable=broad-exception-caught

def calculate_and_print(a, b, operation_name):
    """Calculate and print function for calculator."""
    operation_mapping = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mapping.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("ERROR: Division by zero.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    """Main function to parse arguments and run the calculator."""
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()
