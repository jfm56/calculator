"""Test to ensure calculator functions properly."""
from decimal import Decimal
from calculator import calculations

#Test calculations

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
