"""Basic arithmetic operations: addition, subtraction, multiplication, and division."""
from decimal import Decimal
from typing import Callable

#pylint: disable=unnecessary-dunder-call, invalid-name

class calculations:
    """Preforms arthmic operations as static methosds"""

    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        """Return the difference of two numbers."""
        return a - b

    @staticmethod
    def multiply (a: Decimal,b: Decimal) -> Decimal:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Returns the quotient of two numbers. Raises an error when dividing by zero."""
        if b == Decimal("0"):
            raise ZeroDivisionError("ERROR: Division by zero")
        return a / b

    @staticmethod
    def calculation(a: Decimal,
                    b: Decimal,
                    operation: Callable[[Decimal, Decimal], Decimal])-> Decimal:
        """Dynamically preforms calculation using provided operation"""
        return operation(a,b)
