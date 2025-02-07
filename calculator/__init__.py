"""Basic arithmetic operations: addition, subtraction, multiplication, and division."""
from decimal import Decimal

def add(num1: Decimal,num2: Decimal) -> Decimal:
    """Return the sum of two numbers."""
    return num1 + num2

def subtract(num1: Decimal,num2: Decimal) -> Decimal:
    """Return the difference of two numbers."""
    return num1 - num2

def multiply (num1: Decimal,num2: Decimal) -> Decimal:
    """Return the product of two numbers."""
    return num1 * num2

def divide (num1: Decimal,num2: Decimal) -> Decimal:
    """Return the quotent of two numbers."""
    return num1 / num2
