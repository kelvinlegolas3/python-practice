# Assessment 6  : Object Oriented Programming v2
# Link          : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/04-OOP%20Challenge.ipynb

# 1.
print("Exercise # 1:")

class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Deposit Accepted. Your balance now is: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return f"Withdrawal Accepted. Your balance now is {self.balance}"
        else:
            return f"Attempted withdraw amount is: {amount}. Your remaning balance is only {self.balance}"
        
    

account1 = Account("Jose", 100)
print(account1.owner)
print(account1.balance)
print(account1)
print(account1.deposit(200))
print(account1.withdraw(300))
print(account1.withdraw(300))