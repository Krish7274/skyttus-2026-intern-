#1 - Create a car class with attributes like brand,model,and speed,and methods to accelerate/brake..
class car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model 
        self.speed = speed
    def accelerate(self, value):
        self.speed += value
        print(f"Speed increased to {self.speed} km/h")
    def brake(self,value):
        self.speed -= value
        if self.speed < 0:
          self.speed = 0
        print(f"Speed decreased to {self.speed} km/h")
car1 = car("Toyota", "Fortuner")

car1.accelerate(30)
car1.accelerate(20)
car1.brake(25)


#2 - Create a Bank Account Class With deposit and withdraw methods..
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.accouny_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdrawalcamount must br positive")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current balance: {self.balance}")
account1 = BankAccount("Krish Patel", 10000)
account1.deposit(5000)
account1.withdraw(3000)
account1.withdraw(15000)

#3 - Create a student class with a method to calculate average marks..
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_average(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        return average
student1 = Student("Krish Patel", [80,85,95,84])
avg = student1.calculate_average()
print("Average Marks:", avg)

#4 - Create a Rectangle class with methods to find area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
rect1 = Rectangle(10, 5)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

#5 - Create an Employee class that displays salary details.
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_salary_details(self):
        print(f"Employee Name  : {self.name}")
        print(f"Employee ID    : {self.employee_id}")
        print(f"salary         : {self.salary}")
emp1 = Employee("Krish Patel", 101, 50000)
emp1.display_salary_details()

#6 - Create a Book class to store title, author, and price, and display details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display_details(self):
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price  : {self.price}")
book1 = Book("Python Programming", "Krish Patel", 650)
book1.display_details()

#7 - Create a Circle class to find area and circumference.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def circumference(self):
        return 2 * math.pi * self.radius
circle1 = Circle(7)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())

#8 - Create a Laptop class with a method to apply discounts on price.
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount
        print(f"Discount Applied: {discount_percent}%")
        print(f"Final Price: {self.price}")
laptop1 = Laptop("Dell", "Inspiron", 60000)
laptop1.apply_discount(10)

#9 - Create a Flight class with seat booking functionality.
class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self, seats):
        if seats <= 0:
            print("Invalid number of seats")
        elif self.booked_seats + seats > self.total_seats:
            print("Not enough seats available")
        else:
            self.booked_seats += seats
            print(f"{seats} seat(s) booked successfully")

    def available_seats(self):
        return self.total_seats - self.booked_seats
flight1 = Flight("AI-202", 100)

flight1.book_seat(3)
flight1.book_seat(5)

print("Available seats:", flight1.available_seats())

#10 - Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []

    def add_product(self, product_name, price):
        self.products.append((product_name, price))
        print(f"Product '{product_name}' added successfully")

    def list_products(self):
        print(f"\nProducts in {self.shop_name}:")
        if not self.products:
            print("No products available")
        else:
            for product, price in self.products:
                print(f"- {product} : ₹{price}")
shop1 = Shop("Krish Store")

shop1.add_product("Laptop", 60000)
shop1.add_product("Mobile", 20000)
shop1.add_product("Headphones", 1500)

shop1.list_products()
