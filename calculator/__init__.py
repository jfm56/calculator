"""Basic arithmetic operations: addition, subtraction, multiplication, and division."""
from decimal import Decimal
from typing import Callable

#pylint: disable=unnecessary-dunder-call, invalid-name

class CalculationHistory:
    """Encapsulates a single calculation with two numbers and an operation."""

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initialize a calculation.

        Args:
            a (Decimal): First number.
            b (Decimal): Second number.
            operation (Callable[[Decimal, Decimal], Decimal]): Function that performs the operation.
        """
        self.a = a
        self.b = b
        self.operation = operation

    def compute(self) -> Decimal:
        """Executes the calculation and returns the result."""
        return self.operation(self.a, self.b)



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
