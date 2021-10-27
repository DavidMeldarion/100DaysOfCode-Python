# Import data from data file
from data import MENU,MONEY,resources

# Define functions
def print_resources(resources):
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f"{key.title()}: {value}ml")
        elif key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key == "money":
            print(f"{key.title()}: ${value}")

def check_resources(MENU,resources,user_input):
    item=MENU[user_input]
    ingredients=item["ingredients"]
    for key,value in ingredients.items():
        if value <= resources[key]:
            enough=True
        elif value > resources[key]:
            return key
    return enough

def insert_coins():
    print("Please insert coins.")
    quarters=float(input("How many quarters?: "))
    dimes=float(input("How many dimes?: "))
    nickles=float(input("How many nickles?: "))
    pennies=float(input("How many pennies?: "))
    total_input= round(quarters*.25,2) + round(dimes*.1,2) + round(nickles*.05,2) + round(pennies*.01,2)
    return total_input

def enough_money(coins, MENU, user_input):
    item = MENU[user_input]
    if coins >= item["cost"]:
        return True
    else:
        return False

def make_drink(MENU,resources,user_input,coins):
    drink=MENU[user_input]
    cost=drink["cost"]
    diff=coins-cost
    resources["money"]+=cost
    for key, value in drink["ingredients"].items():
        resources[key]-=value
    return round(diff,2)

machine_on=True
while machine_on:
    user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        machine_on=False
        print("Shutting down. Goodbye!")

    elif user_input == "report":
        print_resources(resources)
    
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        is_enough=check_resources(MENU,resources,user_input)
        if is_enough == True:
            coins=insert_coins()
            enough_coins=enough_money(coins,MENU,user_input)
            if enough_coins == True:
                change=make_drink(MENU,resources,user_input,coins)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        elif is_enough != True:
            print(f"Sorry, there is not enough {is_enough}")
    else:
        print("Invalid input. Try again.")