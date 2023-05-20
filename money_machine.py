class MoneyMachine():

    def __init__(self) -> None:
        self.__currency = "$"
        self.__coin_values = {
            "penny": 0.01,
            "nickel": 0.05,
            "dime": 0.1,
            "quarter": 0.25
        }
        self.__profit = 0
        self.__money_received = 0
    
    def report(self) -> None:
        print(f"Money: {self.__currency}{self.__profit}")

    def process_coins(self) -> float:
        print("Please insert coins: ")
        for x in self.__coin_values:
            self.__money_received += (int(input(f"{x}: ")) * self.__coin_values[x]) 
        return self.__money_received
    
    def make_payments(self, cost:float) -> bool:
        self.process_coins()
        if self.__money_received < cost:
            print("Sorry that's not enough money. Money refunded.")
            self.__money_received = 0
            return False
        else:
            change = round(self.__money_received - cost, 2)
            print(f"Here is {self.__currency}{change} in change")
            self.__profit += cost
            self.__money_received = 0
            return True 