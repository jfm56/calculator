"""Operations for conftest"""

#pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal

def add(a: Decimal, b: Decimal)-> Decimal:
    """Test add function"""
    return a + b

def subtract(a: Decimal, b: Decimal)-> Decimal:
    """Test subtract function"""
    return a - b

def multiply(a: Decimal, b: Decimal)-> Decimal:
    """Test multiply function"""
    return a * b

def divide(a: Decimal, b: Decimal)-> Decimal:
    """Test divide function"""
    if b == 0:
        raise ZeroDivisionError("ERROR: Division by zero")
    return a / b
