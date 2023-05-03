# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def check_resources(drink):
#     ingredients = MENU[drink]["ingredients"]
    
#     if ingredients.get("milk") is not None :
#         drink_milk = ingredients["milk"]
#     drink_water = ingredients["water"]
#     drink_coffee = ingredients["coffee"]
    
#     if drink_water > resources["water"]:
#         print("Sorry there is not enough water.")
#     elif drink_coffee > resources["coffee"]:
#         print("Sorry there is not enough coffee.")
#     elif ingredients.get("milk") is not None and drink_milk > resources["milk"]:
#         print("Sorry there is not enough milk.")
#     else:
#         return True

# def process_drink(drink):
#     if check_resources(drink=drink):
#         ingredients = MENU[drink]["ingredients"]
#         if ingredients.get("milk") is not None:
#             resources["milk"] -= ingredients["milk"]
#         resources["water"] -= ingredients["water"]
#         resources["coffee"] -= ingredients["coffee"]
#         return resources
    

# def process_coins(price, drink):
#     print("Please insert coins.")
#     quarter = int(input("how many quarters?:"))
#     dimes = int(input("how many dimes?:"))
#     nickles = int(input("how many nickles?:"))
#     pennies = int(input("how many pennies?:"))

#     total = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

#     if total > price:
#         print(f"Here is ${round(total-price)} in change.")
#         print(f"Here is your {drink} ☕️. Enjoy!")
#     elif total < price:
#         print("Sorry that's not enough money. Money refunded.")
#         return 0
#     return money + total

# def report():
#     print("Water: ",resources["water"]," ml")
#     print("Milk: ", resources["milk"], " ml")
#     print("Coffee: ", resources["coffee"], " ml")
#     print("Money: $" ,round(money))

# turn_off = False
# money = 0

# while not turn_off:
#     user_choice = input("What would you like? (espresso/latte/cappuccino):")
#     if user_choice == "report":
#         report()
#     elif user_choice == "off":
#         turn_off = True
#     else:
#         new_resources = process_drink(user_choice)
#         if new_resources:
#             money = process_coins(MENU[user_choice]["cost"], user_choice)
            

# Define the menu of drinks and their ingredients and prices
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Define the initial amount of resources available in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Define a function to check if there are enough resources to make a drink


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    
    # Check if there is enough water, coffee, and milk (if required) to make the drink
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

# Define a function to process a drink request and update the resources accordingly
def process_drink(drink):
    if check_resources(drink=drink):
        ingredients = MENU[drink]["ingredients"]

        # If milk is required for the drink, deduct the required amount from the resources
        if ingredients.get("milk") is not None:
            resources["milk"] -= ingredients["milk"]

        # Deduct the required amount of water and coffee from the resources
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]

        # Return the updated resources dictionary
        return resources

# Define a function to process a user's coins and dispense their drink


def process_coins(price, drink):
    print("Please insert coins.")
    quarter = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))

    # Calculate the total amount of money inserted by the user
    total = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    # Check if the user has inserted enough money to buy the drink
    if total > price:
        # Calculate and print the amount of change to give to the user
        print(f"Here is ${round(total-price)} in change.")
        # Dispense the drink and print a message telling the user to enjoy it
        print(f"Here is your {drink} ☕️. Enjoy!")
    elif total < price:
        # If the user has not inserted enough money, print an error message and return 0
        print("Sorry that's not enough money. Money refunded.")
        return 0
    # If the user has inserted exactly the right amount of money, return the total amount of money inserted
    return money + total

# Define a function to print a report of the current resources and money in the machine


def report():
    print("Water: ", resources["water"], " ml")
    print("Milk: ", resources["milk"], " ml")
    print("Coffee: ", resources["coffee"], " ml")
    print("Money: $", round(money))


# Initialize the turn_off variable to False and the money variable to 0
turn_off = False
money = 0

# Start a loop that allows users to select drinks until they turn off the machine
while not turn_off:
    # Prompt the user to select a drink or enter "report" or "off"
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    # If the user enters "report", print a report of the current resources and money
    if user_choice == "report":
        report()
    # If the user enters "off", set turn_off to True to end the loop
    elif user_choice == "off":
        turn_off = True
    else:
        # If the user selects a drink, process the drink request and update the resources
        new_resources = process_drink(user_choice)
        # If there are enough resources, process the user's coins and update the money variable
        if new_resources:
            money = process_coins(MENU[user_choice]["cost"], user_choice)
