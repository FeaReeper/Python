# import pets

class Ninja:
    pet_food = 100

    def __init__(self, first_name, last_name, treats, pet_food):
        self.fname = first_name
        self.lname = last_name
        self.treats = treats
        self.food = pet_food
        self.pet = Pet('Mr. Blue', 'Duck', 'swimming')

    def walk(self):
        self.pet.play()
        return self

    def feed(self, amount_food):
        if amount_food < self.pet_food:
            self.pet.eat(self.treats, self.food)
        else:
            print("Time to head to the duck store for more food")
        return self

    def bathe(self):
        print('Pet is clean')
        self.pet.noise('quack quack')
        return self
    
    def display(self):
        self.pet.display_stats()

class Pet:
    energy = 20
    health = 20

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self):
        self.energy += 25
        print(f'{self.name} is sleeping')
        return self

    def eat(self, treat, food):
        self.energy += 5
        self.health += 10
        print(f'{self.name} is eating {treat} and {food}')
        return self

    def play(self):
        self.health += 5
        self.energy -= 10  #I added this because it made sense to me
        print(f'{self.name} is {self.tricks}')
        return self

    def noise(self, sound):
        print(sound)
        return self
    
    def display_stats(self):
        print(f'Health: {self.health}' + '\n' + f'Energy: {self.energy}')
        return self


matthew = Ninja('Billy', 'Madison', 'gummy bears', 'other ducks')

matthew.feed(150).walk().bathe().display()


