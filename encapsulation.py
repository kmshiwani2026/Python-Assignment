# 2/11/26
# Encapsulation

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self._salary = salary


#     def get_salary(self):
#         return self._salary


#     def inc_salary(self,amount):
#         if amount >0:
#             self._salary += amount
#             print("Salary updated")
#         else:
#             print("Invalid amount")
# emp=Employee("Shailesh",25,50000)
# print("Salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:",emp.get_salary())

# Inheritance

# single inheritance

# class Animal():
#     def property (self):
#         print("Animal has 4 legs")

# class  Dog(Animal):

#     def bark(self):
#         print("Dog barks")

# d=Dog()
# d.bark()
# d.property()

# Multiple inheritance

# class Father():

#     def skill1(self):
#         print("Driving")

# class Mother():

#     def skill2(self):
#         print("cooking")

# class child(Father,Mother):

#     def Qualities(self):
#         print("Inherited skills from parents:")

# x=child()
# x.Qualities()
# x.skill1()
# x.skill2()





# multilevel inheritance
 
# class Grandfather():

#     def house(self):
#         print("Grandfather's house")

# class Father(Grandfather):

#     def bike(self):
#         print("Father's bike")

# class Son(Grandfather):

#     def laptop(self):
#         print("Son's Laptop")


# class Grandson(Father,Son):
        
#     def car(self):
#         print("Grandson's car")


# g=Grandson()
# g.house()
# g.bike()
# g.laptop()






#Hierarchial Inheritance

# class Institute():

#     def name(self):
#         print("NSTIW ALLAHABAD")

# class Teacher(Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass


# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name()

# Classwork

# 2/11/26

# 1:Student Management System — Single Inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)


# student1 = Student("Shivani", 20, 101, "AIPA")

# student1.display_student()

# 2:Bank Account System — Single Inheritance

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited Amount:", amount)


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         return interest

#     def display_details(self):
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", self.calculate_interest())


# account1 = SavingAccount(12345, 10000, 5)

# account1.deposit(2000)
# account1.display_details()


# 3:Family Assets — Multilevel Inheritance
# class Grandfather:
#     def house(self):
#         print("Grandfather has a House")


# class Father(Grandfather):
#     def bike(self):
#         print("Father has a Bike")


# class Son(Father):
#     def laptop(self):
#         print("Son has a Laptop")


# son1 = Son()

# son1.house()
# son1.bike()
# son1.laptop()

# 4:Employee Hierarchy — Multilevel Inheritance
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         print("Name:", self.name)


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary_amount = salary

#     def salary(self):
#         print("Salary:", self.salary_amount)


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

#     def display_details(self):
#         self.get_name()
#         self.salary()
#         self.team_size_details()

#     def team_size_details(self):
#         print("Team Size:", self.team_size)


# manager1 = Manager("Shivani", 50000, 10)

# manager1.display_details()


# 5:College Management System — Hierarchical Inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display_student(self):
#         self.display_details()
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_teacher(self):
#         self.display_details()
#         print("Subject:", self.subject)


# student1 = Student("Shivani", 20, 85)
# teacher1 = Teacher("Anita", 35, "Python")

# print("Student Details:")
# student1.display_student()

# print("\nTeacher Details:")
# teacher1.display_teacher()

# 6:Vehicle Management System — Hierarchical Inher 
# class Vehicle:
#     def start(self):
#         print("Vehicle is Starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has Air Conditioning")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is Required for Bike")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Bus Capacity: 50 Passengers")


# # Creating Objects

# car1 = Car()
# bike1 = Bike()
# bus1 = Bus()

# print("Car Details:")
# car1.start()
# car1.air_condition()

# print("\nBike Details:")
# bike1.start()
# bike1.helmet_required()

# print("\nBus Details:")
# bus1.start()
# bus1.passenger_capacity()


# 7:Smart Phone System — Multiple Inheritance
# class Camera:
#     def take_photo(self):
#         print("Taking a Photo")


# class MusicPlayer:
#     def play_music(self):
#         print("Playing Music")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Making a Phone Call")


# # Creating Object

# phone1 = SmartPhone()

# phone1.take_photo()
# phone1.play_music()
# phone1.make_call()


# 8:Working Student — Multiple Inheritance
# class Student:
#     def study(self):
#         print("Student is Studying")


# class Employee:
#     def work(self):
#         print("Employee is Working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Working Student is Managing Time")


# # Creating Object

# student1 = WorkingStudent()

# student1.study()
# student1.work()
# student1.manage_time()


# 9:Company Structure — Hybrid Inheritance
# class Employee:
#     def attendance(self):
#         print("Employee Attendance Marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Developer is Writing Code")


# class Tester(Employee):
#     def test_software(self):
#         print("Tester is Testing Software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Team Lead is Managing Team")


# # Creating Object

# team1 = TeamLead()

# team1.attendance()
# team1.write_code()
# team1.test_software()
# team1.manage_team()


# 10:Educational Institute — Hybrid Inheritance
# class Person:
#     def display_name(self):
#         print("Name: Shivani")


# class Student(Person):
#     def study(self):
#         print("Student is Studying")


# class Teacher(Person):
#     def teach(self):
#         print("Teacher is Teaching")


# class Mentor(Student, Teacher):
#     def guide(self):
#         print("Mentor is Guiding Students")


# # Creating Object

# mentor1 = Mentor()

# mentor1.display_name()
# mentor1.study()
# mentor1.teach()
# mentor1.guide()












































