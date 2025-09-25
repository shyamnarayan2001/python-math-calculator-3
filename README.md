# Python Math Calculator

A simple command-line calculator application that performs basic mathematical operations on two numbers.

## Features

- **Addition** of two numbers
- **Subtraction** of two numbers
- **Input validation** and error handling
- **User-friendly** command-line interface
- **Continuous operation** until user chooses to exit

## File Structure

```
python-math-calculator-3/
├── main.py          # Main application with user interface
├── calculator.py    # Core calculator class with math operations
├── utils.py        # Utility functions for input validation
└── README.md       # Project documentation
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/shyamnarayan2001/python-math-calculator-3.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python-math-calculator-3
   ```

3. Run the main application:
   ```bash
   python main.py
   ```

## Usage

1. Run the application
2. Select an operation from the menu:
   - **1**: Addition
   - **2**: Subtraction
   - **3**: Exit
3. Enter two numbers when prompted
4. View the result
5. Choose to perform another calculation or exit

## Example Usage

```
Welcome to Python Math Calculator!

========================================
    PYTHON MATH CALCULATOR
========================================
Available operations:
1. Addition (+)
2. Subtraction (-)
3. Exit
========================================
Select operation (1-3): 1

Selected: Addition
Enter first number: 15.5
Enter second number: 23.7

------------------------------
Operation: Addition
Calculation: 15.5 + 23.7 = 39.2
Result: 39.2
------------------------------

Do you want to perform another calculation? (y/n): n

Thank you for using Python Math Calculator!
Goodbye!
```

## Code Structure

### Calculator Class (`calculator.py`)
- `add(a, b)`: Returns the sum of two numbers
- `subtract(a, b)`: Returns the difference of two numbers

### Utility Functions (`utils.py`)
- `is_valid_number(input_str)`: Validates if input can be converted to a number
- `parse_number(input_str)`: Converts string input to float with error handling
- `get_number_input(prompt)`: Gets validated number input from user

### Main Application (`main.py`)
- `display_menu()`: Shows available operations
- `get_operation_choice()`: Gets user's operation selection
- `perform_calculation()`: Executes the selected math operation
- `display_result()`: Formats and displays calculation results
- `main()`: Main application loop

## Error Handling

The application includes robust error handling for:
- Invalid numeric input (non-numeric characters)
- Invalid operation selection
- User input validation with retry prompts

## Requirements

- Python 3.x (no external dependencies required)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.
