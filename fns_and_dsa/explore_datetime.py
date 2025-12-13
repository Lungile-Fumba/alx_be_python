import datetime

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    and saves the current date (YYYY-MM-DD) in a variable.
    """
    # Get the current datetime object
    current_datetime = datetime.datetime.now()
    
    # Format for full date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Save just the current date (YYYY-MM-DD) in a variable
    current_date = current_datetime.strftime("%Y-%m-%d")
    
    # Print the current date and time
    print(f"Current date and time: {formatted_datetime}")
    
    # Return the current_date for use in other functions
    return current_date


def calculate_future_date(days_to_add):
 
   
    current_datetime_obj = datetime.datetime.now()
    

    future_datetime_obj = current_datetime_obj + datetime.timedelta(days=days_to_add)
    

    future_date = future_datetime_obj.strftime("%Y-%m-%d")
    

    print(f"Future date: {future_date}")
    
    return future_date


if __name__ == "__main__":
  
    current_date = display_current_datetime()
    
   
