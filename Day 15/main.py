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
# TODO - 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#[x] a. Check the user’s input to decide what to do next.
#[x] b. The prompt should show every time action has completed, e.g. once the drink is dispensed
#[x] c. The prompt should show again to serve the next customer.

# TODO - 2. Turn off the Coffee Machine by entering “off” to the prompt.
# [x] a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
#       Your code should end execution when this happens.

# TODO - 3. Print report.
# [x] a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
#           Water: 100ml
#           Milk: 50ml
#           Coffee: 76g
#           Money: $2.5
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

# TODO - 4. Check resources sufficient?
#[x] a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
#[x] b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
#       It should not continue to make the drink but print: “Sorry there is not enough water.”
#[x] c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO - 5. Process coins.
#[x] a. If there are sufficient resources to make the drink selected, then the program should
#     prompt the user to insert coins.

#[x] b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

#[x] c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#     pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO - 6. Check transaction successful?

#[x] a. Check that the user has inserted enough money to purchase the drink they selected.
#  E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#  program should say “Sorry that's not enough money. Money refunded.”.

#[x] b. But if the user has inserted enough money, then the cost of the drink gets added to the
#  machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5

#[x] c. If the user has inserted too much money, the machine should offer change.
#       E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#       places.

# TODO - 7. Make Coffee.

#[x] a. If the transaction is successful and there are enough resources to make the drink the
#       user selected, then the ingredients to make the drink should be deducted from the
#       coffee machine resources.
#   E.g. report before purchasing latte:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#       Money: $0
#   Report after purchasing latte:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5

#[x] b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.