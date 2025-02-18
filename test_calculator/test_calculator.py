"""Test to ensure calculator functions properly."""
from decimal import Decimal
from calculator import Calculator

#Test calculations

def test_add():
    """Test to see if add function works."""
    assert Calculator.add(Decimal("2"), Decimal("2")) == Decimal("4")

def test_subtract():
    """Test to see if subtraction function works."""
    assert Calculator.subtract(Decimal("2"), Decimal("2")) == Decimal("0")

def test_multiply():
    """Test to see if multiply function works."""
    assert Calculator.multiply(Decimal("2"), Decimal("2")) == Decimal("4")

def test_divide():
    """Test to see if division function works."""
    assert Calculator.divide(Decimal("2"),Decimal("2")) == 1
