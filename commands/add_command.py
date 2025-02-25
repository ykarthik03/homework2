from decimal import Decimal, InvalidOperation
from commands.base_command import BaseCommand
from calculator import Calculator

class AddCommand(BaseCommand):
    def name(self) -> str:
        return "add"

    def execute(self, *args) -> None:
        """
        Usage:
          add <number1> <number2>
        """
        if len(args) != 2:
            print("Error: 'add' requires exactly two numbers. Example: add 2 3")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = Calculator.add(a, b)
            print(f"Result of add {a} and {b} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid input. Please provide valid numbers. Received: {list(args)}")
        except Exception as e:
            print(f"Error while performing addition: {e}")
