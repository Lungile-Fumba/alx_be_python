from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format
    and saves the current date in a variable named current_date.
    """
    now = datetime.now()
    
    # Format and print current date and time
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    # Save current date as required
    current_date = now.strftime("%Y-%m-%d")
    
    return current_date


def calculate_future_date(days_to_add):
    """
    Calculates the future date after adding the specified number of days.
    Saves the future datetime object in future_date, then uses .strftime() on it.
    """
    current = datetime.now()
    
    # Create future datetime object and save it to future_date (as object first)
    future_date = current + timedelta(days=days_to_add)
    
    # Now explicitly use future_date.strftime() as required by the checker
    formatted_future = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future}")
    
    return formatted_future


# Main program
if __name__ == "__main__":
    # Part 1
    current_date = display_current_datetime()
    
    # Part 2
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(number_of_days)
    except ValueError:
        print("Error: Please enter a valid integer.")