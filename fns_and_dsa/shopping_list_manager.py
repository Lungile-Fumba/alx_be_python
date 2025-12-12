
shopping_list = []

print("Welcome to the Shopping List Manager!")

while True:

    
        print("Shopping List Menu")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View current list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":

            item = input("Enter the item to add: ").strip()
            if item:  
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print(" You didn't enter anything. Item not added.")
    
        elif choice == "2":
        
            if not shopping_list:
                print("Your shopping087 list is empty. Nothing to remove.")
            else :
                    item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"'{item_to_remove}' was not found in the shopping list.")
    
        elif choice == "3":
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\nYour Current Shopping List:")
                print("-" * 25)
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
            print(f"\nTotal items: {len(shopping_list)}")
    
        elif choice == "4":
            print("Thank you for using the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
shopping_list()
    

