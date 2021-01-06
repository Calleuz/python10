import os    

class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            if os.path.getsize(filepath) > 0:
                self.balance = float(file.read())
            else: 
                with open(filepath, 'w') as emptyfile:
                    self.balance = 0.0
                    emptyfile.write('0.0')
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file: 
            file.write(str(self.balance))

# account = Account("balance.txt")

# print(account.balance)
# account.deposit(100)
# account.withdraw(400)
# account.commit()
# print(account.balance)

# Inheritance
class Checking(Account):

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)
    
    def transfer(self, amount):
        self.balance -= (amount + self.fee)


checking = Checking("balance.txt", 12)
checking.transfer(100)
checking.commit()
print(checking.balance)


    