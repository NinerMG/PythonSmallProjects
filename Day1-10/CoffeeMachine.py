resources = {"water": 300, "milk": 200, "coffee": 100, "money":0}

MENU = {
    "espresso":{"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()

        if choice == "off":
            print("Turning off coffee machine")
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                money_received = process_coins()
                if transaction_successful(money_received, choice):
                    make_coffee(choice)
        else:
            print("Invalid selection. Please try again.")

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(drink):
        for item, amount in MENU[drink]["ingredients"].items():
            if resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

def process_coins():
    print("Please insert coins.")
    coins = float(input())
    return coins


def transaction_successful(money_received, drink):
    cost = MENU[drink]["cost"]
    if money_received < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(money_received - cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    resources["money"] += cost
    return True

def make_coffee(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Here is your {drink}. Enjoy!")