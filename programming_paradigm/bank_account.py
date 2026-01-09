class BankAccount: 
    def __init__(self, initial_balance):
        if initial_balance < 0:
           raise ValueError("Initial balance cannot be negative!")
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        self.account_balance += amount 
        print( f"Deposited: ${amount}")
        
    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0: 
            return print("Insufficient Funds") 
        print(f"Withdrew: ${amount}")

    def display_balance(self):
        print (f"Current Balance: ${self.account_balance:.2f}")

