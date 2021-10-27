from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

COFFEE_MAKER=CoffeeMaker()
MONEY_MACHINE=MoneyMachine()
MENU=Menu()
machine_on=True
while machine_on == True:
    user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_input == "off":
        machine_on=False
        print("Shutting down. Goodbye!")

    elif user_input == "report":
        COFFEE_MAKER.report()
        MONEY_MACHINE.report()

    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink=MENU.find_drink(user_input)
        MENU_ITEM=drink.name
        if drink == "None":
            print("Invalid input. Try again.")
        is_enough=COFFEE_MAKER.is_resource_sufficient(drink)
        if is_enough == True:
            enough_coins=MONEY_MACHINE.make_payment(drink.cost)
            if enough_coins == True:
                COFFEE_MAKER.make_coffee(drink)
        