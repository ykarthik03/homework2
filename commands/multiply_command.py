from decimal import Decimal, InvalidOperation
from commands.base_command import BaseCommand
from calculator import Calculator

class MultiplyCommand(BaseCommand):
    def name(self) -> str:
        return "multiply"

    def execute(self, *args) -> None:
        """
        Usage:
          multiply <number1> <number2>
        """
        if len(args) != 2:
            print("Error: 'multiply' requires exactly two numbers. Example: multiply 2 3")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = Calculator.multiply(a, b)
            print(f"Result of multiply {a} and {b} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid input. Please provide valid numbers. Received: {list(args)}")
        except Exception as e:
            print(f"Error while performing multiplication: {e}")
