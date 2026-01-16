#1 - Create a base class Animal and subclasses Dog and Cat.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("The Animal Makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meoww.!!")
dog1 = Dog("Rocky")
cat1 = Cat("Daisy")
dog1.speak()
cat1.speak()


#2 - Create a class hierarchy for Vehicle->Car-> ElectricCar.

class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")
ev = ElectricCar()
ev.start()
ev.drive()
ev.charge()

#3 -  method overriding in a base and derived class.

class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.sound()
d.sound()

#4 - Demonstrate multiple inheritance with two parent classes.

class Father:
    def skills(self):
        print("Father: Driving")
class Mother:
    def skills(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skills()

#5 - Create a polymorphic function that works with different shapes.

class Rectangle:
    def area(self):
        return 10 * 5
class Circle:
    def area(self):
        return 3.14 * 7 * 7
def print_area(Shape):
    print("Area:", Shape.area())
r = Rectangle()
c = Circle()
print_area(r)
print_area(c)

#6 - Create a Bank system with SavingsAccount and CurrentAccount classes.

class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")
class SavingsAccount(BankAccount):
        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient balance in saving Account")
            else:
                self.balance -= amount
                print(f"Withdrawn {amount} from Savings. Balance: {self.balance}")
class CurrentAccount(BankAccount):
     def withdraw(self, amount):
          self.balance -= amount
          print(f"Withdrawn {amount} from Current. Balance: {self.balance}")
s = SavingsAccount(101, 50000)
c = CurrentAccount(102, 30000)
s.deposit(10000)
s.withdraw(70000)
c.deposit(2000)
c.withdraw(60000)

#7 - Create a class with private attributes and getter/setter methods.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__ = name
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
p = Person("Krish Patel", 21)
print(p.get_name())
print(p.get_age())
p.set_age(22)
print(p.get_age())

#8 - Create a Teacher and Student class to show inheritance.

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def display_info(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
class Student(Teacher):
    def __init__(self, name, subject, roll_no):
        super().__init__(name, subject)
        self.roll_no = roll_no
    def display_student_info(self):
        self.display_info()
        print("Roll No:", self.roll_no)
s1 = Student("Krish Patel", "Python", 76)
s1.display_student_info()


#9 - Create a MusicPlayer class and subclass Spotify to override play method.

class MusicPlayer:
    def play(self):
        print("Playing music from Music player")
class Spotify(MusicPlayer):
        def play(self):
            print("Playing music on spotify")
player = MusicPlayer()
spotify = Spotify()
player.play()
spotify.play()

#10 - Demonstrate the use of super() in inheritance.

class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    def show(self):
        super().show()
        print("Roll No:", self.roll_no)
s = Student("Krishh Patel", 76)
s.show()
              
