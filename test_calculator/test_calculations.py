"""
Test to ensure proper calculator history functions.
"""

from decimal import Decimal
import pytest
from calculator.calculations import CalculationHistory


def test_calculation_history_addition_stored():
    """Test that addition calculations are stored in history."""
    CalculationHistory.clear_history()
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x + y)
    CalculationHistory.history.append(calc)
    assert CalculationHistory.get_history() == [calc]


def test_calculation_history_multiple_entries():
    """Test multiple calculations are stored in history."""
    CalculationHistory.clear_history()

    calc1 = CalculationHistory(Decimal("2"), Decimal("3"), lambda x, y: x * y)
    calc2 = CalculationHistory(Decimal("10"), Decimal("2"), lambda x, y: x / y)

    CalculationHistory.history.append(calc1)
    CalculationHistory.history.append(calc2)

    history = CalculationHistory.get_history()
    assert len(history) == 2
    assert history == [calc1, calc2]


def test_calculation_history_get_last():
    """Test retrieving the last calculation from history."""
    CalculationHistory.clear_history()

    calc1 = CalculationHistory(Decimal("5"), Decimal("5"), lambda x, y: x + y)
    calc2 = CalculationHistory(Decimal("10"), Decimal("2"), lambda x, y: x - y)

    CalculationHistory.history.append(calc1)
    CalculationHistory.history.append(calc2)

    assert CalculationHistory.get_last_calculation() is calc2


def test_calculation_history_clear():
    """Test clearing calculation history."""
    CalculationHistory.clear_history()
    calc1 = CalculationHistory(Decimal("6"), Decimal("3"), lambda x, y: x / y)
    calc2 = CalculationHistory(Decimal("4"), Decimal("2"), lambda x, y: x - y)

    CalculationHistory.history.append(calc1)
    CalculationHistory.history.append(calc2)

    assert len(CalculationHistory.get_history()) == 2
    CalculationHistory.clear_history()
    assert not CalculationHistory.get_history()  # ✅ Fixes Pylint warning


def test_calculation_history_compute_addition():
    """Test calculation history for addition."""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x + y)
    assert calc.compute() == Decimal("15")


def test_calculation_history_compute_subtraction():
    """Test calculation history for subtraction."""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x - y)
    assert calc.compute() == Decimal("5")


def test_calculation_history_compute_multiplication():
    """Test calculation history for multiplication."""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x * y)
    assert calc.compute() == Decimal("50")


def test_calculation_history_compute_division():
    """Test calculation history for division."""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x / y)
    assert calc.compute() == Decimal("2")


def test_calculation_history_division_by_zero():
    """Test calculator divide by zero function."""
    with pytest.raises(ZeroDivisionError):
        calc = CalculationHistory(Decimal("10"), Decimal("0"), lambda x, y: x / y)
        calc.compute()

def test_calculation_repr():
    """Test string representation (__repr__) of CalculationHistory."""
    calc = CalculationHistory(Decimal("5"), Decimal("3"), lambda x, y: x + y)
    expected_repr = "Calculation(5, 3, <lambda>)"
    assert repr(calc) == expected_repr
