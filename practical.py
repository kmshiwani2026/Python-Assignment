# Rectangle pattern
# for i in range(1, 5):
#     for j in range(1,7):
#         print("*", end=" ")
#     print()  

# Increasing Triangle
# for r in range(1, 8):
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print()

# Number square
# for p in range(1, 5):
#     for k in range(1, 5):
#         print(p, end=" ")
#     print()

# Classroom Seating
# for i in range(1, 6):
#     for j in range(1, 9):
#         print("R" + str(i) + "S" + str(j), end=" ")
#     print()

#Prime number
# for i in range(2, 51):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i, end=" ")

 #Patter challange Centered pyramid
# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(" ", end="")
#     for k in range(1, 2*i):
#         print("*", end="")
#     print()

# Tables 2 to 10
for i in range (2,11):
    print("Table for" ,i)
    for j in range(1,11):
        multiply = i*j
        print(i, "*",j,"=", multiply)

    # while i <= 20:
     
    # if i == 12:
    #    i += 2
       
    # print(i)
    # i += 2

# calculator program

# print("My calculator !")
# print("Type 'exit' to quit")

# while True:

#     op=input("Enter operation (+,-,*,/ or exit):")
#     if op == "exit":
#         print("calculator closed!")
#         break
#     num1=float(input("Enter first number:"))
#     num2=float(input("Enter second number:"))

#     if op == "+":
#         print(num1,"+",num2,"=",num1+num2)
#     elif op == "-":
#         print(num1,"-",num2,"=",num1-num2)
#     elif op == "*":
#         print(num1,"*",num2,"=",num1*num2)
#     elif op == "/":
#         print(num1,"/",num2,"=",num1/num2)
#     else:
#      print("Invalid operation")