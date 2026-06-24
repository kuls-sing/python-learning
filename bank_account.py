class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New balance: {self.balance} ")
    
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def __str__(self):
        return f"Account owner: {self.owner_name} | Balance: {self.balance}"
    
acc1 = BankAccount("Alice", 1000)
print(acc1)
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)
print(acc1)