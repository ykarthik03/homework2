"""Tests for the basic arithmetic operations."""

import pytest
from app.operations import add, subtract, multiply, divide

def test_add():
    """Test the addition operation."""
    assert add(2, 3) == 5

def test_subtract():
    """Test the subtraction operation."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Test the multiplication operation."""
    assert multiply(2, 3) == 6

def test_divide():
    """Test the division operation."""
    assert divide(6, 3) == 2

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        divide(6,0)
