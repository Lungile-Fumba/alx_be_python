class BankAccount: 
    def __init__(self, initial_balance):
        if initial_balance < 0:
           raise ValueError("Initial balance cannot be negative!")
        self.account_balance = float(initial_balance)
    
    def deposit(self, ammount):
        self.account_balance += ammount 
        print( f"Deposited: {ammount}")
        
    def withdraw(self, ammount):
        self.account_balance -= ammount
        if self.account_balance < 0: 
            return print("Insufficient Funds") 
        print(f"Withdrew: {ammount}")

    def display_balance(self ):
        print (f"Current Balance: {self.account_balance}")