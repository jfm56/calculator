"""
Operations for calculator including storing history and managing history.
"""

from decimal import Decimal
from typing import Callable

class CalculationHistory:
    """Encapsulates a single calculation with two numbers and an operation."""

    history: list["CalculationHistory"] = []  # Class-level history storage

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
    def get_history(cls) -> list["CalculationHistory"]:
        """Returns a copy of the calculation history or an empty list if no history exists."""
        return cls.history[:] if cls.history else []


    @classmethod
    def get_last_calculation(cls) -> "CalculationHistory | None":
        """Returns the most recent calculation or None if history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """Clears calculation history."""
        cls.history.clear()

    def __repr__(self):
        """Returns a string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
