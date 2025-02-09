"""Test to ensure calculator functions properly."""
from decimal import Decimal
from calculator import CalculationHistory, calculations


#Test CalculationHistory

def test_calculation_history_addition():
    """Test claculation history for addition"""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x + y)
    assert calc.compute()== Decimal("15")

def test_calculation_history_subtraction():
    """Test calculation history for subtraction"""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x - y)
    assert calc.compute()== Decimal("5")

def test_calculation_history_multiplication():
    """Test calculation history for multiplication"""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x * y)
    assert calc.compute()== Decimal("50")


def test_add():
    """Test to see if add function works."""
    assert calculations.add(Decimal("2"), Decimal("2")) == Decimal("4")

def test_subtract():
    """Test to see if subtraction function works."""
    assert calculations.subtract(Decimal("2"), Decimal("2")) == Decimal("0")

def test_multiply():
    """Test to see if multiply function works."""
    assert calculations.multiply(Decimal("2"), Decimal("2")) == Decimal("4")

def test_divide():
    """Test to see if division function works."""
    assert calculations.divide(Decimal("2"),Decimal("2")) == 1
