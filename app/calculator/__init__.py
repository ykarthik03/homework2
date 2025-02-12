"""Calculator Module - Contains the main Calculator class."""
from typing import Tuple
from app.operations import (
    add as add_operation,
    subtract as subtract_operation,
    multiply as multiply_operation,
    divide as divide_operation,
    Calculation,
    Calculations
)

class Calculator:
    """Calculator class providing arithmetic operations with history tracking."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers and store the calculation."""
        result = add_operation(a, b)
        calculation = Calculation("add", (a, b), result)
        Calculations.add_calculation(calculation)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and store the calculation."""
        result = subtract_operation(a, b)
        calculation = Calculation("subtract", (a, b), result)
        Calculations.add_calculation(calculation)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and store the calculation."""
        result = multiply_operation(a, b)
        calculation = Calculation("multiply", (a, b), result)
        Calculations.add_calculation(calculation)
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide a by b and store the calculation."""
        result = divide_operation(a, b)
        calculation = Calculation("divide", (a, b), result)
        Calculations.add_calculation(calculation)
        return result

    @staticmethod
    def get_last_calculation() -> Tuple[str, Tuple[float, float], float]:
        """Get the last calculation performed."""
        calc = Calculations.get_last_calculation()
        if calc is None:
            raise ValueError("No calculations in history")
        return calc.operation, calc.operands, calc.result