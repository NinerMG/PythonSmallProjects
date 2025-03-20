import random
from prettytable import PrettyTable

import CoffeeMachine


def main():
   evenNumber()

def greetings():
    name = input("Enter your name")
    print(f"Hello,", name)

def checkType():
    name = "Maciek"
    number = 2
    decimalNumber = 2.0

    print(type(name))
    print(type(number))
    print(type(decimalNumber))

def isFullAge():
    age = int(input("Enter your age"))
    if age >= 18:
        print("You welcome")
    else:
        print("You are under age!")

def randomList():
    owoce = ["jabłko", "banan", "gruszka", "truskawka", "borówka", "wiśnia"]
    print(random.choice(owoce))

def evenNumber():
    for i in range(1, 20):
        if i % 2 == 0:
            print(i)


if __name__ == '__main__':
  CoffeeMachine.coffee_machine()