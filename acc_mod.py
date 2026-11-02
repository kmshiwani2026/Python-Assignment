# Access modifiers

# class Student:
#     def __init__(self):
#         self.name = "Shivani"
#         self._trade = "AIPA"
#         self.__marks = 85

#     def show_marks(self):
#       return self.__marks
            
# std = Student()
# print("Name:", std.name)
# print("Trade:",std._trade)
# print("Marks:",std.show_marks())

class Bank_Account:
    def __init__(self,account_name,balance):
        self.account_name=account_name
        self.__balance=balance

    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            print("Deposite Succesfully")
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount <=0:
            print("Invalid Amount")
        elif amount <=self.__balance:
            self.__balance -=amount
            print("Withdrawl successful")
        else:
            print("Insufficiet Amount")

    def check_balance(self):
        print("Current_balance:",self.__balance)
    
user=Bank_Account("Shivani",1000)
user.deposit(500)
user.withdraw(1200)
user.check_balance()
    