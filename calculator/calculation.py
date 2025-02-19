from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Create a new Calculation instance."""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        # Optionally, handle division by zero or other operations here.
        if self.operation.__name__ == 'divide' and self.b == Decimal('0'):
            raise ValueError("Cannot divide by zero")
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        # Provide a meaningful representation if needed.
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
