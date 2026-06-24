class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount
              
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient funds!")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def __str__(self):
        return f"Account owner: {self.owner_name} | Balance: {self.__balance}"


acc1 = BankAccount("Alice", 1000)
print(acc1)
acc1.deposit(500)
acc1.withdraw(200)

  # test encapsulation
acc1.set_balance(-500)       # should be rejected
print(acc1.get_balance())    # should still be 1300
acc1.__balance = -5000       # try direct access — will NOT work
print(acc1.get_balance())    # should still be 1300