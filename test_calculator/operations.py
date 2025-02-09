"""Test to ensure proper calculator history functions"""
from decimal import Decimal
import pytest
from calculator import operations
from calculator.operations import CalculationHistory



#Test CalculationHistory

def test_calculation_history_addition():
    """Test claculation history for addition"""
    calc = CalculationHistory(Decimal("10"), Decimal("5"), lambda x,y: x + y)
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
