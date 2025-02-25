from decimal import Decimal, InvalidOperation
from commands.base_command import BaseCommand
from calculator import Calculator

class DivideCommand(BaseCommand):
    def name(self) -> str:
        return "divide"

    def execute(self, *args) -> None:
        """
        Usage:
          divide <number1> <number2>
        """
        if len(args) != 2:
            print("Error: 'divide' requires exactly two numbers. Example: divide 10 2")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = Calculator.divide(a, b)
            print(f"Result of divide {a} and {b} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid input. Please provide valid numbers. Received: {list(args)}")
        except ValueError as e:
            print(f"Error while performing division: {e}")
        except Exception as e:
            print(f"Error while performing division: {e}")
