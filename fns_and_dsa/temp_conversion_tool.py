FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


unit = float(input("Enter the temperature to convert: "))


convert = input("Tempature in Celsius or Is this temperFahrenheit? (C/F): ").strip().lower()

if convert == 'c':

    temp = unit * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{unit}°C is {temp}°F " )

elif convert == "f":

    temp = unit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{unit}°F is {temp}°C " )


else:
    
    print( f"{convert} is an invalid temparture")   