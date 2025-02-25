from decimal import Decimal, InvalidOperation
from commands.base_command import BaseCommand
from calculator import Calculator

class SubtractCommand(BaseCommand):
    def name(self) -> str:
        return "subtract"

    def execute(self, *args) -> None:
        """
        Usage:
          subtract <number1> <number2>
        """
        if len(args) != 2:
            print("Error: 'subtract' requires exactly two numbers. Example: subtract 5 3")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = Calculator.subtract(a, b)
            print(f"Result of subtract {a} and {b} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid input. Please provide valid numbers. Received: {list(args)}")
        except Exception as e:
            print(f"Error while performing subtraction: {e}")
