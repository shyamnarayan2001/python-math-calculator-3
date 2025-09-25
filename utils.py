# utils.py - Utility functions for input validation

def is_valid_number(input_str):
    """
    Check if input string can be converted to a valid number.
    
    Args:
        input_str (str): Input string to validate
        
    Returns:
        bool: True if valid number, False otherwise
    """
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def parse_number(input_str):
    """
    Convert string input to number (float).
    
    Args:
        input_str (str): Input string to convert
        
    Returns:
        float: Converted number
        
    Raises:
        ValueError: If input cannot be converted to number
    """
    if not is_valid_number(input_str):
        raise ValueError(f"Invalid number: {input_str}")
    return float(input_str)


def get_number_input(prompt):
    """
    Get a valid number input from user with validation.
    
    Args:
        prompt (str): Prompt message for user
        
    Returns:
        float: Valid number from user
    """
    while True:
        try:
            user_input = input(prompt)
            return parse_number(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
