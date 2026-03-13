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