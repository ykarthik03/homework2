# tests/test_calculator.py
from decimal import Decimal
from calculator import Calculator

def test_addition():
    """Test that the addition function works."""
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    """Test that the subtraction function works."""
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_division():
    """Test that the division function works."""
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_multiplication():
    """Test that the multiplication function works."""
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_divide_by_zero():
    """Test division by zero."""
    try:
        Calculator.divide(Decimal('10'), Decimal('0'))
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
