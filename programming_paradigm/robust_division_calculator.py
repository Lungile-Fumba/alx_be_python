
def safe_divide(numerator, denominator):
  
    try:
        x = float(numerator)
        y = float(denominator)
        results = x / y
        return f"The result of the division is{results:.1f}"
    
    except ValueError:  
        return "Error: Please enter numeric values only."

    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        

