


class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: Charging a $5 fee.")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
            return self

account1 = BankAccount(1.01, 100)
account2 = BankAccount(1.025, 100)

account1.deposit(50).deposit(100).deposit(150).withdraw(200).yield_interest().display_account_info()
account2.deposit(200).deposit(150).withdraw(150).withdraw(20).withdraw(30).withdraw(50).yield_interest().display_account_info()