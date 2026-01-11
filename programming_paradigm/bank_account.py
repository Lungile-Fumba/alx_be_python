class BankAccount: 
    def __init__(self, initial_balance):
        if initial_balance < 0:
           raise ValueError("Initial balance cannot be negative!")
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        """Deposit the specified amount."""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")


    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.1f}")
        return True


    def display_balance(self):
        print (f"Current Balance: ${self.account_balance:1f}")


d = BankAccount(100)

d.deposit(50)

