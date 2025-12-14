import sys

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

FAHRENHEIT_FREEZING_OFFSET = 32



def convert_to_celsius(fahrenheit):

    celsius = (fahrenheit - FAHRENHEIT_FREEZING_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius   

def convert_to_fahrenheit(celsius):
  
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_OFFSET
    return fahrenheit

def main():

    temp_input = input("Enter the temperature to convert: ")
    
    try:

        temperature = float(temp_input)

    except ValueError:
        
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
        
    else:
        # Handle invalid unit input
        print(f"Error: Invalid unit '{unit}'. Please enter 'C' or 'F'.")
        # Exit the script cleanly after an error
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")