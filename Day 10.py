# Day 10
# Inheritence

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print("New balance after withdrawl : ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("New balance after deposit : ", self.balance)


class Savings_account(Account):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest_rate = interest

    def add_interest(self):
        self.balance += self.balance*(self.interest_rate)/100
        print("New balance after adding interest : ", self.balance)


class Checking_account(Account):
    def __init__(self, name, balance, mini=500):
        super().__init__(name, balance)
        self.min_bal = mini

    def withdraw(self, amount):
        if((self.balance-amount) < self.min_bal):
            print("Not enough balance")
        else:
            self.balance -= amount
            print("New balance after withdrawl : ", self.balance)


c = Checking_account("Ben", 2000)
s = Savings_account("Meehan", 3000, 5)

c.withdraw(1900)
s.add_interest()
