Task = input("Enter your task: ")

Priority = input( "Priority (high/medium/low : ").lower()

Time_Bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:

    case "high":

        if Time_Bound  == "yes":

            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")

        else:
            print(f"Reminder: '{Task}' is a high priority task. Please attend to it as soon as possible.")

    case "medium":
        
        print( f"Reminder: '{Task}' is a {Priority} priority task that requires attention today")

    case "low":
        
        print( f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time")





print()