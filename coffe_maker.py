from menu import MenuItem

class CoffeeMaker():

    def __init__(self, water:int=300, milk:int=200, coffee:int=100) -> None:
        self.__resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

    def report(self) -> None:
        print(f"Water: {self.__resources['water']}ml")
        print(f"Milk: {self.__resources['milk']}ml")
        print(f"Coffee: {self.__resources['coffee']}g")

    def is_resource_sufficient(self, drink) -> bool:
        for x in drink.ingredients:
            if drink.ingredients[x] > self.__resources[x]:
                print(f"Sorry there is not enough {x}")
                return False
        return True
    
    def make_coffee(self, order) -> None:
        for x in order.ingredients:
            self.__resources[x] -= order.ingredients[x]
        print(f"Here is your {order.name}. Enjoy!")