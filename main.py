# main.py - Main application with user interface

from calculator import Calculator
from utils import get_number_input


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("    PYTHON MATH CALCULATOR")
    print("="*40)
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Exit")
    print("="*40)


def get_operation_choice():
    """
    Get user's choice of operation.
    
    Returns:
        int: User's choice (1, 2, or 3)
    """
    while True:
        try:
            choice = int(input("Select operation (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1-3).")


def perform_calculation(operation, num1, num2):
    """
    Perform the selected calculation.
    
    Args:
        operation (int): Operation choice (1 for add, 2 for subtract)
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        tuple: (operation_name, result)
    """
    calc = Calculator()
    
    if operation == 1:
        result = calc.add(num1, num2)
        return "Addition", result
    elif operation == 2:
        result = calc.subtract(num1, num2)
        return "Subtraction", result


def display_result(operation_name, num1, num2, result):
    """
    Display the calculation result in a formatted way.
    
    Args:
        operation_name (str): Name of the operation
        num1 (float): First number
        num2 (float): Second number
        result (float): Calculation result
    """
    print(f"\n{"-"*30}")
    print(f"Operation: {operation_name}")
    
    if operation_name == "Addition":
        print(f"Calculation: {num1} + {num2} = {result}")
    elif operation_name == "Subtraction":
        print(f"Calculation: {num1} - {num2} = {result}")
    
    print(f"Result: {result}")
    print(f"{"-"*30}")


def main():
    """Main application loop."""
    print("Welcome to Python Math Calculator!")
    
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice == 3:
            print("\nThank you for using Python Math Calculator!")
            print("Goodbye!")
            break
        
        # Get numbers from user
        print(f"\nSelected: {'Addition' if choice == 1 else 'Subtraction'}")
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        # Perform calculation
        operation_name, result = perform_calculation(choice, num1, num2)
        
        # Display result
        display_result(operation_name, num1, num2, result)
        
        # Ask if user wants to continue
        while True:
            continue_choice = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_choice in ['y', 'yes']:
                break
            elif continue_choice in ['n', 'no']:
                print("\nThank you for using Python Math Calculator!")
                print("Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
