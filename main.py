# main.py
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(a: str, b: str, operation_name: str):
    """Perform a calculation and print the result."""
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        operation = operation_mappings.get(operation_name)
        if operation:
            result = operation(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Entry point for the program."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()