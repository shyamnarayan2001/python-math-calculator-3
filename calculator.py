# calculator.py - Core mathematical operations module

class Calculator:
    """A simple calculator class for basic mathematical operations."""
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """
        Subtract second number from first number.
        
        Args:
            a (float): First number (minuend)
            b (float): Second number (subtrahend)
            
        Returns:
            float: Difference of a and b
        """
        return a - b
