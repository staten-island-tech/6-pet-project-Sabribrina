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

""" class Hero:
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
print(Yaotose_Hinako.__dict__) """

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__ (self, name, email, student_id):
        super().__init__(name, email) # Call the parent class constructor
        self.student_id = student_id

    def display_info (self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__ (self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def display_info (self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__ (self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def display_info (self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"

    def manage_system (self):
        return f"{self.name} ({self.role} is managing the yuriful system.)"

student = Student("Sebastian", "sebby@yuri.com", "S609")
teacher = Teacher("Mrs. Annika", "ann@yuri.com", "Mathematics")
my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
administrator = Administrator("Mr. V", "vex@yuri.com", "Principal")
admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Sebastian, Email: sebby@yuri.com, Student ID: S609
print(teacher.display_info())  # Output: Teacher: Mrs. Annika, Email: ann@yuri.com, Subject: Mathematics
print(my_teacher.display_info())  # Output: User: Mr. Brown, Email: brown@example.com, Subject: Science
print(administrator.display_info())  # Output: Administrator: Mr. V, Email: vex@yuri.com, Role: Principal
print(admin.manage_system())  # Output: Ms. Johnson (Principal) is managing the system.