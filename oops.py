# 28/10/25
# OOPS concept
# class Aipa:
#     def __init__(self,name,roll_no,trade,marks): #__init__= constructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks

# std1=Aipa("shivi","1","AIPA",90)
# std2=Aipa("Avi",2,"AIPA",90)

# print(std1.name)
# print(std1.roll_no)
# print(std1.trade)
# print(std1.marks)

# print(std2.name)
# print(std2.roll_no)
# print(std2.trade)
# print(std2.marks)


# class Student:
#     def __init__(self, name, roll_no, trade, marks):
#          self.name = name
#          self.roll_no = roll_no
#          self.trade = trade
#          self.marks = marks

#     def display_details(self):
#         print("Name",self.name)
#         print("Roll No",self.roll_no)
#         print("Trade:",self.trade) 
#         print("Marks:",self.marks)


#     def check_result(self):
#         if self.marks >=40:
#           print("pass")
#         else:
#           print("Fail")

#     def percentage(self,total_marks):
#         return (self.marks/total_marks)*100

# student1=Student("Anushka",1,"AIPA",75)       
# student2=Student("Aditya",2,"AIPA",85)

# student1.display_details()
# student1.check_result()
# print(student1.percentage(100), "%")
# student2.display_details()
# student2.check_result()


# class Car:
#     def __init__(self, brand, model, color, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Price:", self.price)

#     def check_price(self):
#         if self.price >= 500000:
#             print("Expensive Car")
#         else:
#             print("Affordable Car")

#     def discount(self, discount_percent):
#         return self.price - (self.price * discount_percent / 100)


# car1 = Car("Maruti", "Swift", "White", 600000)
# car2 = Car("Tata", "Punch", "Black", 450000)

# car1.display_details()
# car1.check_price()
# print("Price after 10% discount:", car1.discount(10))

# print("--------------------")

# car2.display_details()
# car2.check_price()
# print("Price after 10% discount:", car2.discount(10))
