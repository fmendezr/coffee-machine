menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}

money = 0

# Check whether there are enough resources to make a drink
def enough_resources (drink_name):
    for ingredient in menu[drink_name]["ingredients"]:
        if menu[drink_name]["ingredients"][ingredient] > resources[ingredient]:
            return False
    return True

# Report how many resources are left
def report():
    print(f"""Water: {resources['water']}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}""")

report()