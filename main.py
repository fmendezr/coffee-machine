from menu import Menu
from money_machine import MoneyMachine
from coffe_maker import CoffeeMaker

if __name__ == "__main__":

    #initialize class instances
    menu = Menu()
    money_machine = MoneyMachine()
    coffe_maker = CoffeeMaker()

    # main loop 
    while True:
        drink_name = input(f"What would you like to order? ({menu.get_items()}): ")
        if drink_name == "OFF":
            print("Turning Coffee Machine Off")
            break 
        if drink_name == "report":
            coffe_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(drink_name)
        if drink == None:
            continue
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payments(drink.cost):
                coffe_maker.make_coffee(drink)
            else: continue
        



        
            

