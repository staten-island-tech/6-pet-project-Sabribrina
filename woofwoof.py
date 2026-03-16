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

class Hero:
    def __init__ (self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy (self, item):
        self.inventory.append(item)
        print(self.inventory)

""" Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy({"title": "sword", "atk": 34})
print(Jillian.__dict__ ) """

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # double underscore means "private"
        
    def deposit(self, amount):
        self.__balance += amount
    
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

Yaotose_Hinako = Hero("Yaotose Hinako", 500, ["Yashiro Miko"])
Yaotose_Hinako.buy({"title": "Oumi Shiori (Mermaid)", "atk": 999999})
print(Yaotose_Hinako.__dict__)

class Pet:
    def __init__ (self, name, happiness):
        self.name = name
        self.happiness = happiness