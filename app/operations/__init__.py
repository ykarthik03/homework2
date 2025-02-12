"""Operations Module - Contains basic arithmetic operations and Calculation class."""
from typing import Tuple, Optional, List
from dataclasses import dataclass

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@dataclass
class Calculation:
    """Class to store calculation details."""
    operation: str
    operands: Tuple[float, float]
    result: Optional[float] = None

class Calculations:
    """Class to manage calculation history."""
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Add a calculation to history."""
        cls._history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Get the most recent calculation."""
        return cls._history[-1] if cls._history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clear calculation history."""
        cls._history.clear()