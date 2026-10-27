# 1: Age Verification System
# try:
#     age = int(input("Enter your age: "))

#     if age < 0 or age > 120:
#         raise ValueError("Age must be between 0 and 120")

#     print("Valid age:", age)

# except ValueError as e:
#     print("Error:", e)


# 2: Product Price Checker
# try:
#     price = float(input("Enter product price: "))

#     if price < 0:
#         raise ValueError("Price cannot be negative.")

#     print("Valid price:", price)

# except ValueError as e:
#     print("Error:", e)


# 3: Tuple Element Access
# cities = ("Delhi", "Mumbai", "Kolkata", "Chennai", "Jaipur", "Lucknow", "Prayagraj")
# try:
#     position = int(input("Enter position (0-6): "))
#     print("City:", cities[position])

# except IndexError:
#     print("Error: Invalid position.")

# except ValueError:
#     print("Error: Please enter an integer.")


# 4: Contact Information Lookup
# contacts = {
#     "Shivani": "9876543210",
#     "Riya": "9876501234",
#     "Neha": "9123456789"
# }

# try:
#     name = input("Enter contact name: ")
#     print("Phone Number:", contacts[name])

# except KeyError:
#     print("Error: Contact not found.")


# 5: File Writing Operation
# try:
#     filename = input("Enter filename: ")
#     text = input("Enter text: ")

#     with open(filename, "w") as file:
#         file.write(text)

#     print("Text written successfully.")

# except PermissionError:
#     print("Error: Permission denied.")


# 6: Valid Roll Number Input
# while True:
#     try:
#         roll_no = int(input("Enter student roll number: "))

#         if roll_no <= 0:
#             raise ValueError("Roll number must be greater than zero.")

#         print("Valid Roll Number:", roll_no)
#         break

#     except ValueError as e:
#         print("Error:", e)


# 7: Custom Exception for Voting Eligibility
# class NotEligibleToVoteError(Exception):
#     pass


# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise NotEligibleToVoteError("You are not eligible to vote.")

#     print("You are eligible to vote.")

# except NotEligibleToVoteError as e:
#     print("Error:", e)


# 8: Bank Account Deposit Validation
# try:
#     amount = float(input("Enter deposit amount: "))

#     if amount <= 0:
#         raise ValueError("Deposit amount must be greater than zero.")

#     print("Deposit successful:", amount)

# except ValueError as e:
#     print("Error:", e)


# 9: Shopping Cart Quantity Check
# try:
#     quantity = int(input("Enter item quantity: "))

#     if quantity < 1:
#         raise ValueError("Quantity must be at least 1.")

#     print("Valid quantity:", quantity)

# except ValueError as e:
#     print("Error:", e)


# 10: Password Strength Validator
# try:
#     password = input("Enter password: ")

#     if len(password) < 8:
#         raise ValueError("Password must contain at least 8 characters.")

#     print("Password is valid.")

# except ValueError as e:
#     print("Error:", e)


# 11: Student Grade Calculator
# try:
#     m1 = float(input("Enter marks for Subject 1: "))
#     m2 = float(input("Enter marks for Subject 2: "))
#     m3 = float(input("Enter marks for Subject 3: "))

#     marks = [m1, m2, m3]

#     for mark in marks:
#         if mark < 0 or mark > 100:
#             raise ValueError("Marks must be between 0 and 100.")

#     average = sum(marks) / 3

#     if average >= 90:
#         grade = "A"
#     elif average >= 75:
#         grade = "B"
#     elif average >= 60:
#         grade = "C"
#     elif average >= 40:
#         grade = "D"
#     else:
#         grade = "F"

#     print("Average Marks:", average)
#     print("Grade:", grade)

# except ValueError as e:
#     print("Error:", e)


# 12: ATM PIN Verification
# correct_pin = "1234"

# try:
#     for attempt in range(3):
#         pin = input("Enter PIN: ")

#         if pin == correct_pin:
#             print("PIN verified successfully.")
#             break
#         else:
#             print("Incorrect PIN.")

#     else:
#         raise ValueError("Three unsuccessful attempts. Access denied.")

# except ValueError as e:
#     print("Error:", e)


# 13: Email Address Validator
# try:
#     email = input("Enter email address: ")

#     if "@" not in email or "." not in email:
#         raise ValueError("Invalid email address.")

#     print("Valid email address.")

# except ValueError as e:
#     print("Error:", e)


# 14: Division of List Elements
# numbers = [10, 20, 30, 40, 50]

# try:
#     index1 = int(input("Enter first index: "))
#     index2 = int(input("Enter second index: "))

#     result = numbers[index1] / numbers[index2]

#     print("Result:", result)

# except IndexError:
#     print("Error: Invalid index.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter an integer.")


# 15: Username Availability Checker
# class UsernameAlreadyExistsError(Exception):
#     pass


# existing_usernames = ["shivani", "riya", "neha", "pooja"]

# try:
#     username = input("Enter username: ")

#     if username in existing_usernames:
#         raise UsernameAlreadyExistsError("Username already exists.")

#     print("Username is available.")

# except UsernameAlreadyExistsError as e:
#     print("Error:", e)


# 16: Electricity Bill Calculator
# try:
#     units = float(input("Enter units consumed: "))

#     if units < 0:
#         raise ValueError("Units cannot be negative.")

#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = units * 7
#     else:
#         bill = units * 10

#     print("Electricity Bill:", bill)

# except ValueError as e:
#     print("Error:", e)


# 17: Student Record Search
# students = {
#     "101": {"name": "Shivani", "marks": 85},
#     "102": {"name": "Riya", "marks": 78},
#     "103": {"name": "Neha", "marks": 90}
# }

# try:
#     student_id = input("Enter student ID: ")
#     print("Student Details:", students[student_id])

# except KeyError:
#     print("Error: Student record not found.")


# 18: Mobile Number Validation
# try:
#     mobile = input("Enter mobile number: ")

#     if len(mobile) != 10 or not mobile.isdigit():
#         raise ValueError("Mobile number must contain exactly 10 digits.")

#     print("Valid mobile number.")

# except ValueError as e:
#     print("Error:", e)


# 19: Online Ticket Booking
# class SeatsNotAvailableError(Exception):
#     pass


# available_seats = 10

# try:
#     tickets = int(input("Enter number of tickets: "))

#     if tickets > available_seats:
#         raise SeatsNotAvailableError("Requested tickets exceed available seats.")

#     print("Booking successful.")
#     print("Tickets booked:", tickets)
#     print("Remaining seats:", available_seats - tickets)

# except SeatsNotAvailableError as e:
#     print("Error:", e)

# except ValueError:
#     print("Error: Please enter a valid number.")


# 20: Number Range Validator
# try:
#     number = int(input("Enter a number between 1 and 50: "))

#     if number < 1 or number > 50:
#         raise ValueError("Number must be between 1 and 50.")

#     print("Valid number:", number)

# except ValueError as e:
#     print("Error:", e)