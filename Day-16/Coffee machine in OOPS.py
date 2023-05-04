from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes
machine = Menu()
coffee_maker = CoffeeMaker()
machine_money = MoneyMachine()
is_on = True

while is_on:
    # Ask the user to choose their drink
    user_drink = input(f"please choose your drink {machine.get_items()} : ")
    if user_drink == "off":
        # Exit loop if user chooses "off"
        is_on = False
    elif user_drink == "report":
        # Report the status of the coffee maker and money machine
        coffee_maker.report()
        machine_money.report()
    else:
        # Find the drink the user requested
        drink = machine.find_drink(user_drink)

        # Check if the coffee maker has enough resources to make the drink
        if coffee_maker.is_resource_sufficient(drink):

            # Check if the user has enough money to make the payment
            if machine_money.make_payment(drink.cost):
                # Make the drink if the payment is successful
                coffee_maker.make_coffee(drink)
