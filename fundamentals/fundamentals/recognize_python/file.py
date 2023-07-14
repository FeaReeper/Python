num1 = 42   #variable declaration = integer
num2 = 2.3  #variable declaration = integer
boolean = True  #variable declaration = boolean
string = 'Hello World' #variable declaration = string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Composite - List - Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Composite - Dict - Initialize
fruit = ('blueberry', 'strawberry', 'banana') # Composite - Tuples - Initialize
print(type(fruit)) # print to console - type of data for "fruit"
print(pizza_toppings[1]) # print to console - index value at position 1 for pizza_toppings
pizza_toppings.append('Mushrooms') # add 'mushrooms' to pizza_toppings list
print(person['name']) # print to console - the value of key 'name' in person dict
person['name'] = 'George' # change value of name in person dict to 'George'
person['eye_color'] = 'blue' # change value of eye_color in person dict to 'blue'
print(fruit[2]) # print to console - index 2 of fruit tuple - 'banana'

# condition based on the value of num1 being a higher number than 45
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# conditional determining if the length of a given word is less than 5 letters, greater than 15 letters, or in between
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop going through a range of numbers 1-4 and printing each number to console
for x in range(5):
    print(x)
# for loop going through a range of number 2,3,4 and printing each number to console
for x in range(2,5):
    print(x)
# for loop going through 2-9 going by 3's (2,5,8) and printing those numbers to console
for x in range(2,10,3):
    print(x)
# while loop prints x each time until x becomes 5 (prints 0,1,2,3,4)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # this removes the last item in pizza_toppings list
pizza_toppings.pop(1) # this removes item in index 1 in pizza_toppings list

print(person) # print the dictionary person
person.pop('eye_color') # removes the key and value for eye_color in person dict
print(person) #prints the new person dict without the eye color

# this for loop will check all the values in the list and continue if 'Pepperoni' is found and break out of the loop if 'olives' is found
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# function that will print 'Hello' 10 times
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function called

#function that will print 'Hello' as many times as the parameter number is
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # function called with parameter

# this function will print 'Hello' 14 times
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # This passes no parameter so x = 10
print_hello_x_or_ten_times(4) # This passes parameter of 4 so x = 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)


class User:

    def __init__(self) -> None:
        pass