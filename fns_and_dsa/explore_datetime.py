from datetime import datetime, timedelta

def display_current_datetime():

    now = datetime.now()
    
    
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    
   
    current_date = now.strftime("%Y-%m-%d")
    
   
    print(f"Current date and time: {formatted_datetime}")
    

    return current_date


def calculate_future_date(days_to_add):
  
    current_datetime = datetime.now()
    
   
    future_datetime = current_datetime + timedelta(days=days_to_add)
    

    future_date = future_datetime.strftime("%Y-%m-%d")
    
    
    print(f"Future date: {future_date}")
    
    return future_date


if __name__ == "__main__":
    
    current_date = display_current_datetime()
    
    
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(number_of_days)
    except ValueError:
        print("Error: Please enter a valid integer.")
