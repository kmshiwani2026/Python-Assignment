# Practical No. 1: Python Basics and Operators

# Library Membership Program

# Taking input from user
member_name = input("Enter Member Name: ")
age = int(input("Enter Age: "))
borrowed_books = int(input("Enter Number of Books: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Float variable
membership_fee = 500.0

# Assignment operator
borrowed_books += 1

# Membership operator
has_letter_a = 'a' in member_name.lower()

# Identity and logical operators
eligible = (is_student is True) and (age > 17) and (borrowed_books < 5)

# Displaying membership summary
print("\n--- Library Membership Summary ---")
print("Member Name:", member_name)
print("Age:", age)
print("Borrowed Books:", borrowed_books)
print("Student Status:", is_student)
print("Membership Fee:", membership_fee)
print("Contains letter 'a':", has_letter_a)
print("Eligible:", eligible)


