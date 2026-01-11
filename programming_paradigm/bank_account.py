class BankAccount: 
    def __init__(self, initial_balance):
        if initial_balance < 0:
           raise ValueError("Initial balance cannot be negative!")
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        if amount <= 0:
            return False  # Return False for invalid deposit
        self.account_balance += amount
        return True  # Return True for successful deposit

    def withdraw(self, amount):
        if amount <= 0:
            return False
        
        if amount > self.account_balance:
            return False
        
        self.account_balance -= amount
        return True

#   def get_balance(self):
        return self.account_balance

    def display_balance(self):
        print (f"Current Balance: ${self.account_balance:.1f}")