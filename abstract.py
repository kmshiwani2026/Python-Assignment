# 4/11/26

# Abstractmethod

# from abc import ABC,abstractmethod

# class Payment(ABC): 

#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCard(Payment):

#     def pay(self,amount):
#         print("Paid",amount,"using Credit Card")

# class Cash(Payment):

#     def pay(self,amount):
#         print("Paid",amount,"using Cash")

# class UPI(Payment):

#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# p1=UPI()
# p1.pay(1000)

# p2=CreditCard()
# p2.pay(2000)

# p3=Cash()
# p3.pay(3000)
     
# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass

# class Bike(Vehicle):

#     def drive(self):
#         print("Bike is moving")

# class Car(Vehicle):

#     def drive(self):
#         print("Car is moving")

# class Bus(Vehicle):

#     def drive(self):
#         print("Bus is moving")
# car=Car()
# bike=Bike()
# bus=Bus()
# car.drive()
# bike.drive()
# bus.drive()
    

# from abc import ABC, abstractmethod
# import math

# # Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# # Circle Class
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius

# # Rectangle Class
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # Square Class
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# # Creating Objects
# c = Circle(8)
# r = Rectangle(20, 5)
# s = Square(29)

# # Display Areas
# print("Area of Circle =", round(c.area(), 2))
# print("Area of Rectangle =", r.area())
# print("Area of Square =", s.area())

# Bank Account (Abstract Class)

# from abc import ABC, abstractmethod

# # Abstract Class
# class BankAccount(ABC):

#     @abstractmethod
#     def deposit(self):
#         pass

#     @abstractmethod
#     def withdraw(self):
#         pass


# # Savings Account
# class SavingsAccount(BankAccount):

#     def deposit(self):
#         print("Money deposited in Savings Account")

#     def withdraw(self):
#         print("Money withdrawn from Savings Account")


# # Current Account
# class CurrentAccount(BankAccount):

#     def deposit(self):
#         print("Money deposited in Current Account")

#     def withdraw(self):
#         print("Money withdrawn from Current Account")


# # Creating Objects
# s = SavingsAccount()
# c = CurrentAccount()

# # Calling Methods
# s.deposit()
# s.withdraw()

# c.deposit()
# c.withdraw()

# Notification System

# from abc import ABC, abstractmethod

# # Abstract Class
# class Notification(ABC):

#     @abstractmethod
#     def send(self):
#         pass

# # Email Notification
# class EmailNotification(Notification):

#     def send(self):
#         print("Sending Notification through Email")

# # SMS Notification
# class SMSNotification(Notification):

#     def send(self):
#         print("Sending Notification through SMS")

# # WhatsApp Notification
# class WhatsAppNotification(Notification):

#     def send(self):
#         print("Sending Notification through Whatsapp")

# e = EmailNotification()
# e.send()
# s = SMSNotification()
# s.send()
# w = WhatsAppNotification()
# w.send()

# Institute Management

from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):

    @abstractmethod
    def display_details(self):
        pass

class Student(Person):

    def display_details(self):
        print("Student Name: Shivani")
        print("Course: AIPA")

class Teacher(Person):

    def display_details(self):
        print("Teacher Name: Shailesh Yadav")
        print("Subject: Python")

class Principal(Person):

    def display_details(self):
        print("Principal Name: Ajay Pal Singh")
        print("Institute: NSTI ALLAHABAD")

s = Student()
s.display_details()

print()

t = Teacher()
t.display_details()

print()

p = Principal()
p.display_details()


