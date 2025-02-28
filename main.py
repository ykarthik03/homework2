# main.py
import sys
import os
import logging
import logging.config

from decimal import Decimal, InvalidOperation
from calculator import Calculator
from plugin_loader import load_plugins
from environment import ENVIRONMENT, LOG_LEVEL  # Load environment variables

def setup_logging():
    """Configure logging from logging.conf."""
    config_file = 'logging.conf'
    # Ensure the logs directory exists before configuring logging.
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if os.path.exists(config_file):
        # Pass defaults so that %(LOG_LEVEL)s is interpolated correctly.
        logging.config.fileConfig(config_file, disable_existing_loggers=False, defaults={'LOG_LEVEL': LOG_LEVEL})
    else:
        logging.basicConfig(level=LOG_LEVEL)

setup_logging()
logger = logging.getLogger("appLogger")
logger.info("Application starting in %s environment", ENVIRONMENT)

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
            logger.info("Calculation performed: %s %s %s = %s", a, operation_name, b, result)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            logger.warning("Unknown operation requested: %s", operation_name)
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        logger.error("Invalid number input: %s or %s", a, b, exc_info=True)
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        logger.error("Attempted division by zero", exc_info=True)
        print("An error occurred: Cannot divide by zero.")
    except Exception as e:
        logger.exception("An unexpected error occurred")
        print(f"An error occurred: {e}")

def start_repl():
    """
    [Commands Branch] Launches the REPL with extra debug messages.
    """
    commands = load_plugins("commands")
    logger.debug("Starting REPL with commands: %s", list(commands.keys()))
    print("Welcome to the Interactive Calculator (REPL) [Commands Branch]!")
    print("Type 'menu' to list commands or 'exit' to quit.")

    while True:
        user_input = input(">>> ").strip()
        if not user_input:
            continue

        if user_input.lower() == "exit":
            logger.info("Exiting REPL per user request.")
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
            logger.debug("Executing command '%s' with args %s", cmd_name, args)
            commands[cmd_name].execute(*args)
        else:
            logger.warning("Unknown command entered: %s", cmd_name)
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

def test_calculate_and_print_exception(monkeypatch, capsys):
    """
    Force an unexpected exception in Calculator.add to cover the generic exception branch.
    """
    from calculator import Calculator
    from main import calculate_and_print

    # Save the original function
    original_add = Calculator.add

    # Monkey-patch Calculator.add to throw an exception
    Calculator.add = lambda a, b: (_ for _ in ()).throw(Exception("Forced error"))
    
    calculate_and_print("1", "2", "add")
    output = capsys.readouterr().out.strip()
    
    # Check that the output contains the generic error message
    assert "An unexpected error occurred" in output

    # Restore the original function
    Calculator.add = original_add
