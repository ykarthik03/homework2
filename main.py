import sys

from decimal import Decimal, InvalidOperation
from calculator import Calculator
from plugin_loader import load_plugins

def calculate_and_print(a: str, b: str, operation_name: str):
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


def start_repl():
    """
    [Commands Branch] Launches the REPL with extra debug messages.
    """
    commands = load_plugins("commands")
    print("Welcome to the Interactive Calculator (REPL) [Commands Branch]!")
    print("Type 'menu' to list commands or 'exit' to quit.")

    while True:
        user_input = input(">>> ").strip()
        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("[Commands Branch] Exiting REPL...")
            sys.exit(0)

        if user_input.lower() == "menu":
            print("Available commands:")
            for cmd_name in commands.keys():
                print(f"  {cmd_name}")
            continue

        tokens = user_input.split()
        cmd_name = tokens[0]
        args = tokens[1:]
        if cmd_name in commands:
            commands[cmd_name].execute(*args)
        else:
            print(f"[Commands Branch] Unknown command: {cmd_name}. Type 'menu' to see available commands.")

def main():
    """
    [Commands Branch] Entry point: 0 args => REPL; 3 args => single-run mode.
    """
    if len(sys.argv) == 1:
        start_repl()
    elif len(sys.argv) == 4:
        _, a, b, operation = sys.argv
        calculate_and_print(a, b, operation)
    else:
        print("Usage:")
        print("  python main.py <number1> <number2> <operation>")
        print("  OR")
        print("  python main.py  (for REPL mode)")
        sys.exit(1)

if __name__ == '__main__':
    main()