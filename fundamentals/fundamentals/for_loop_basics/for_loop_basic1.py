# 1. Basic - Print all integers from 0 - 150

def basic():
    for x in range(151):
        print(x)

basic()


# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def multiples5():
    for x in range(5,1001):
        if x % 5 == 0:
            print(x)

multiples5()


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print"Coding Dojo"

def dojoWay():
    for x in range(1,101):
        if x % 10 == 0:
            print("Coding Dojo")
        elif x % 5 == 0:
            print("Coding")
        else:
            print(x)

dojoWay()


# 4. Whoa. That sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum

def hugeSucker():
    sum = 0
    for x in range(500001):
        if x % 2 == 0:
            sum += x
    print(sum)

hugeSucker()


# 5. Counting by Fours - Print positive numbers starting at 2018, counting down by 4's.

def down4(num):
    for x in reversed(range(num)):
        if x % 4 == 0 and x % 2 == 0:
            print(x)

down4(2018)

# 6. Flexible counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that 
#    are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexible(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)

flexible(2,9,3)

