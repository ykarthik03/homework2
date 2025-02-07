"""Unit tests for the calculator module."""

from calculator import add, subtract

def test_addition():
    """Tests that add function."""
    assert add(2,2) == 4

def test_subtraction():
    """Tests that add function"""
    assert subtract(2,2) == 0
