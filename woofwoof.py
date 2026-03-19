""" class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers
    
Calculator.add(5,6) """

""" class Hero:
    def __init__ (self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy (self, item):
        self.inventory.append(item)
        print(self.inventory) """

""" Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy({"title": "sword", "atk": 34})
print(Jillian.__dict__ ) """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # double underscore means "private"
        
    def deposit(self, amount):
        self.__balance += amount
    
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

Yaotose_Hinako = Hero("Yaotose Hinako", 500, ["Yashiro Miko"])
Yaotose_Hinako.buy({"title": "Oumi Shiori (Mermaid)", "atk": 999999})
print(Yaotose_Hinako.__dict__) """

""" class Pet:
    def __init__ (self, pet_name, happiness):
        self.pet_name = pet_name
        self.__happiness = happiness
    def play (self, play):
        self.__happiness += int(play)
    def show_status (self):
        print(f"{self.pet_name} and {self.__happiness}")

Woof = Pet("Woof", 0)
Woof.play(play = 10)
print(Woof.__dict__) """

class Hero:
    def __init__ (self, name, money, inventory):
        self.name = name
        self.__money = money
        self.inventory = inventory

    def cost (self, cost):
        self.__money -= int(cost)
        
    def buy (self, item):
        self.inventory.append(item)
        print(self.inventory)

Yaotose_Hinako = Hero("Yaotose Hinako", 500, ["Yashiro Miko"])
Yaotose_Hinako.buy({"title": "Oumi Shiori (Mermaid)", "atk": 999999})
Yaotose_Hinako.cost(cost = 100)
print(Yaotose_Hinako.__dict__)