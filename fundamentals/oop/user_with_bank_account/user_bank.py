# class for User
class User:
    # population of users that will increase by 1 every time an instance occurs for the User class
    population = 0

    # constructor for the instance called for each user with passing parameters
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
        self.account2 = BankAccount(0.02, 0)
        User.population += 1

    def make_deposit(self, checking, savings):
        self.account.deposit(checking)
        self.account2.deposit(savings)
        return self

    def make_withdraw(self, checking, savings):
        self.account.withdraw(checking)
        self.account2.withdraw(savings)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account.balance}")
        print(f"User: {self.name}, Savings Balance: {self.account2.balance}")
        return self
    
    def transfer_money(self, amount, other_user):
        if amount < self.account.balance:
            self.make_withdraw(amount)
            other_user.make_deposit(amount)
        else:
            print("Insufficient Funds!")




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


matthew = User('Matthew', 'matthew@email.com')
nya = User('Nya', 'nya@email.com')

matthew.make_deposit(500, 200).make_withdraw(10, 10).display_user_balance()


print(f'Number of account holders: {User.population}')

