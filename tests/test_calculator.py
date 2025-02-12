"""Tests for the Calculator class."""
import pytest
from app.calculator import Calculator, Calculations

@pytest.fixture(autouse=True)
def clear_calculations():
    """Clear calculation history before each test."""
    Calculations.clear_history()

def test_add_calculation(calculator):
    """Test the addition functionality of the Calculator."""
    assert calculator.add(2, 3) == 5
    last_calculation = Calculations.get_last_calculation()
    assert last_calculation.operation == "add"
    assert last_calculation.operands == (2, 3)
    assert last_calculation.result == 5

def test_subtract_calculation(calculator):
    """Test the subtraction functionality of the Calculator."""
    assert calculator.subtract(5, 3) == 2
    last_calculation = Calculations.get_last_calculation()
    assert last_calculation.operation == "subtract"
    assert last_calculation.operands == (5, 3)
    assert last_calculation.result == 2

def test_multiply_calculation(calculator):
    """Test the multiplication functionality of the Calculator."""
    assert calculator.multiply(4, 3) == 12
    last_calculation = Calculations.get_last_calculation()
    assert last_calculation.operation == "multiply"
    assert last_calculation.operands == (4, 3)
    assert last_calculation.result == 12

def test_divide_calculation(calculator):
    """Test the division functionality of the Calculator."""
    assert calculator.divide(6, 2) == 3
    last_calculation = Calculations.get_last_calculation()
    assert last_calculation.operation == "divide"
    assert last_calculation.operands == (6, 2)
    assert last_calculation.result == 3

def test_divide_by_zero(calculator):
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        calculator.divide(6, 0)

def test_get_last_calculation_empty():
    """Test getting last calculation when history is empty."""
    with pytest.raises(ValueError, match="No calculations in history"):
        Calculator.get_last_calculation()

def test_get_last_calculation(calculator):
    """Test getting last calculation after performing operations."""
    calculator.add(2, 3)
    operation, operands, result = Calculator.get_last_calculation()
    assert operation == "add"
    assert operands == (2, 3)
    assert result == 5