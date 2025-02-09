"""Operations for calculator including storing history and managing history"""
from decimal import Decimal
from typing import Callable
from calculator import calculations

#pylint: disable=unnecessary-dunder-call, invalid-name

class CalculationHistory:
    """Encapsulates a single calculation with two numbers and an operation."""

    history: list["calculations"] = []  #Class-level history storage

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

    @classmethod
    def get_history(cls)-> "calculations":
        "Returns most recent calculations or None if history is empty"
        return cls.history if cls.history else None
