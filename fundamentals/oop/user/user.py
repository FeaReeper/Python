# User class
class User:
    # Constructor for each user with parameters to pass in 
    def __init__(self, first, last, email, age) -> None:
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards = False
        self.gold_points = 0

    def display_info(self):
        print(self.first_name + '\n' + self.last_name + '\n' + self.email + '\n' + str(self.age) + '\n' + str(self.is_rewards) + '\n' + str(self.gold_points) + ' points')
        return self

    def enroll(self):
        if self.is_rewards == True:
            print('User is already a member')
            return self
        else:
            self.is_rewards = True
            self.gold_points += 200
            return self

    def spend_points(self, amount):
        if amount > self.gold_points:
            print('You dont have enough points')
            return self
        else:
            self.gold_points = self.gold_points - amount
            return self

# Users
matthew = User('Matthew', 'Reep', 'matthewreep@email.com', 31)
naomi = User('Naomi', 'Reep', 'naomireep@email.com', 30)
nya  = User('Nyalee', 'Reep', 'nyaleereep@email.com', 0)

matthew.enroll().spend_points(50).display_info()
naomi.enroll().spend_points(80).display_info()
nya.enroll().spend_points(220).display_info()

