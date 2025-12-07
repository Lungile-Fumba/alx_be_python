task = input("Enter your task: ")

priority = input("Priority (high/medium/low : ")

time_Bound = input("Is it time-bound? (yes/no): ")

match Priority:

    case "high":

        if Time_Bound  == "yes":

            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")

        else:
            print(f"Reminder: '{task}' is a high priority task. Please attend to it as soon as possible.")

    case "medium":
        
        print( f"Reminder: '{task}' is a {priority} priority task that requires attention today")

    case "low":
        
        print( f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")

    case _:
        print("Invalid priority entered. Please choose high, medium, or low.")




print()