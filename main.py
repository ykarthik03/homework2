"""Interactive demo program for testing the calculator functionality."""
from app.calculator import Calculator

def display_menu():
    """Display the calculator menu."""
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show last calculation")
    print("6. Exit")
    print("====================")

def get_numbers():
    """Get two numbers from user input."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """Main function to run the calculator demo."""
    calculator = Calculator()
    print("Welcome to the Calculator!")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '6':
            print("Thank you for using the calculator!")
            break

        if choice == '5':
            try:
                operation, operands, result = Calculator.get_last_calculation()
                print(f"\nLast calculation: {operands[0]} {operation} {operands[1]} = {result}")
            except ValueError as e:
                print(f"\nError: {e}")
            continue

        if choice not in ['1', '2', '3', '4']:
            print("\nError: Invalid choice! Please try again.")
            continue

        a, b = get_numbers()
        if a is None or b is None:
            continue

        try:
            if choice == '1':
                result = calculator.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == '2':
                result = calculator.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == '3':
                result = calculator.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == '4':
                result = calculator.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
