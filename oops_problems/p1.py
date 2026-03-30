class BankAccount:
    def __init__(self,owner):
        self._balance=0
        self.owner=owner
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if value> 0:
            self._balance=value
        else:
            raise ValueError("insufiicient balance")

    def deposit(self,amount):
        self._balance += amount
        print("your money was added")

    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance -= amount
            print("your money is withdrwaed")
        else:
            raise ValueError("not enought money in account")

    def get_balance(self):
        return self._balance
# Create account
acc = BankAccount("John")

# Test deposit
acc.deposit(1000)
print(acc.get_balance())  

# Test deposit again
acc.deposit(500)
print(acc.get_balance())  

# Test withdraw
acc.withdraw(400)
print(acc.get_balance())

# Test insufficient funds
acc.withdraw(5000)        

# Test owner name
print(acc.owner)          

# Test setter protection
acc.balance = -500