"""Test to ensure proper calculator history functions"""
from decimal import Decimal
import pytest
from calculator import operations
from calculator.operations import CalculationHistory


#Test CalculationHistory

def test_calculation_history_history_addition():
    """Test addition is stored in history."""
    CalculationHistory.clear_history()  # Start fresh
    calc = operations.CalculationHistory(Decimal("10"), Decimal("5"), lambda x, y: x + y)
    assert CalculationHistory.get_history() == [calc]

def test_calculation_history_history_multiple_entries():
    """Test multiple calculations are stored in history."""
    CalculationHistory.clear_history()
    calc1 = operations.CalculationHistory(Decimal("2"), Decimal("3"), lambda x, y: x * y)
    calc2 = operations.CalculationHistory(Decimal("10"), Decimal("2"),  lambda x, y: x / y)

    history = CalculationHistory.get_history()
    assert len(history) == 2
    assert history[0] == calc1
    assert history[1] == calc2

def test_calculation_history_get_last():
    """Clear history prior to test retrieving the last calculation from history."""
    CalculationHistory.clear_history()

    calc1 = operations.CalculationHistory(Decimal("5"), Decimal("5"), lambda x, y: x + y)
    calc2 = operations.CalculationHistory(Decimal("10"), Decimal("2"), lambda x, y: x - y)
    history = CalculationHistory.get_history()
    assert history[0] is calc1
    assert operations.CalculationHistory.get_last_calculation() is calc2

def test_calculation_history_clear_history():
    """Test clearing calculation history."""
    CalculationHistory.clear_history()
    operations.CalculationHistory(Decimal("6"), Decimal("3"),  lambda x, y: x / y)
    operations.CalculationHistory(Decimal("4"), Decimal("2"), lambda x, y: x - y)

    assert len(CalculationHistory.get_history()) == 2
    CalculationHistory.clear_history()
    assert len(CalculationHistory.get_history()) == 0


def test_calculation_history_addition():
    """Test claculation history for addition"""
    calc = operations.CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x + y)
    assert calc.compute()== Decimal("15")

def test_calculation_history_subtraction():
    """Test calculation history for subtraction"""
    calc = operations.CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x - y)
    assert calc.compute()== Decimal("5")

def test_calculation_history_multiplication():
    """Test calculation history for multiplication"""
    calc = operations.CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x * y)
    assert calc.compute()== Decimal("50")

def test_calculation_history_divison():
    """Test calculation history for division"""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x / y)
    assert calc.compute()== Decimal("2")

def test_claculator_history_division():
    """Test calculator divide by zero function"""
    with pytest.raises(ZeroDivisionError):
        calc = CalculationHistory(Decimal("10"),Decimal("0"), lambda x,y: x /y)
        calc.compute()
