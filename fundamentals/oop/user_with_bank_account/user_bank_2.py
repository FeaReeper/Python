# class for User
class User:
    # population of users that will increase by 1 every time an instance occurs for the User class
    population = 0

    # constructor for the instance called for each user with passing parameters
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        User.population += 1

    def new_account(self,int_rate, balance, account_type = "checking"):
        account = BankAccount(int_rate = 1.02, balance = 0)
        self.accounts[account_type] = account
        return self

    def make_deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdraw(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        return self
    
    def display_user_balance(self, account_type):
        print(self.name)
        self.accounts[account_type].display_account_info()
        return self

    def transfer_money(self, account_1, other_user, account_2, amount):
        if amount < self.accounts[account_1]:
            other_user.accounts[account_2] += amount
            print(f'New Balance: {other_user.balance}')
        else:
            print("Insufficient Funds!")
        return self


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

matthew = User('Matthew', 'matt@email.com')
nya = User('Nya', 'nya@mail.com')

nya.new_account(5,1000)
matthew.new_account(1.02, 0)

nya.make_deposit(1000, "checking").display_user_balance("checking")
matthew.make_deposit(200, "checking").display_user_balance("checking")

matthew.transfer_money('checking', nya, 'checking', 200)
