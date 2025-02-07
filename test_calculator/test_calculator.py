'''Calculator test'''
from calculator import add, subtract, multiply, divide

def test_add():
    '''Test add function'''
    assert add(2,2) == 4

def test_subtract():
    '''Test subtraction function'''
    assert subtract(2,2) == 0

def test_multiply():
    '''Test multiply function'''
    assert multiply(2,2) == 4

def test_divide():
    '''Test division function'''
    assert divide(2,2) == 1
