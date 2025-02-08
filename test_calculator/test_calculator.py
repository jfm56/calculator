"""Test to ensure calculator functions properly."""
from calculator import add, subtract, multiply, divide

def test_add():
    """Test to see if add function works."""
    assert add(2,2) == 4

def test_subtract():
    """Test to see if subtraction function works."""
    assert subtract(2,2) == 0

def test_multiply():
    """Test to see if multiply function works."""
    assert multiply(2,2) == 4

def test_divide():
    """Test to see if division function works."""
    assert divide(2,2) == 1
