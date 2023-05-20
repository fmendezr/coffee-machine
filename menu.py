class MenuItem ():
    def __init__(self, name:str, cost:float, water:int, milk:int, coffee:int) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
    
class Menu ():
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items (self) -> str:
        options = ''
        for x in self.menu:
            options += f"{x.name}/"
        return options

    def find_drink (self, drink:str) -> MenuItem or bool:
        for x in self.menu:
            if x.name != drink:
                continue
            else:
                return x
        print("Sorry the item is not available.")
        return None