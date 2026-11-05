3/11/26

# Polymophism
# class Cashpayment:
#     def pay(self,amount):
#         print("Paid",amount,"using cash")

# class UPIPayment:

#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# class Cardpayment:
#     def pay(self,amount):
#         print("Paid",amount,"using card")

# class Netbanking:
#     def pay(self,amount):
#         print("Paid",amount,"using Netbanking")




# choice=input("Choose payment mrthod (cash/upi/card/netbanking): ")
# if choice =="cash":
#     payment=Cashpayment()
# elif choice =="upi":
#     payment=UPIPayment()
# elif choice =="card":
#     payment=Cardpayment()
# elif choice =="netbanking":
#     payment= Netbanking()
#     exit()

# payment.pay(1000)


class SMS:
    def send(self,message):
        print("Sending massage through SMS:",message)

class Email:
    def send(self,message):
        print("Sending massage through Email:",message)
class Whatsapp:
    def send(self,message):
        print("Sending massage through Whatsapp:",message) 

class Telegram:
    def send(self,message):
        print("Sending massage through Telegram:",message)

message= [
    SMS(),
    Email(),
    Whatsapp(), 
    Telegram(),

]
for m in message:
   m.send("Good Morning Everyone")


   
# choice=input("choose massage methode(SMS/email/whatsapp/telegram): ").lower()
# if choice == "sms":
#     message=SMS()

# elif choice == "email":
#     message = Email()

# elif choice =="whatsapp":
#     message = Whatsapp()

# elif choice == "telegram":
#     message = Telegram()

#     exit()

# message.send("My name is Shivani")



