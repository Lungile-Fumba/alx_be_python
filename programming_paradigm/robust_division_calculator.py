
def safe_divide(numerator, denominator):
  
    try:
        x = float(numerator)
        y = float(denominator)
        results = x / y
        print(f"The result of the division is{results:.1f}")

    
    except ValueError:  
        print("Error: Please enter numeric values only.")

    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        

