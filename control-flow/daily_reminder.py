task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

priority = priority.strip().lower()
time_bound = time_bound.strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have time.")
    
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task that requires attention today")
    
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")
    
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
