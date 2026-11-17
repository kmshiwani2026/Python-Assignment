
# Gym Reception Desk Program

# Accept member details
member_name = input("Enter Member Name: ")
age = int(input("Enter Age: "))
classes_booked = int(input("Enter Classes Booked: "))
monthly_fee = float(input("Enter Monthly Fee: "))

membership = input("Active Membership (yes/no): ").lower()

# Convert membership into Boolean
is_active = membership == "yes"

# Update booked classes
classes_booked += 1

# Membership operator
name_check = 'e' in member_name.lower()

# Identity and logical operators
eligible = (age > 15) and (classes_booked < 4)

# Display member summary
print("\n--- Gym Member Summary ---")
print("Member Name:", member_name)
print("Age:", age)
print("Classes Booked:", classes_booked)
print("Monthly Fee: Rs.", monthly_fee)
print("Active Membership:", is_active)
print("Letter 'e' in Name:", name_check)
print("Eligible:", eligible)

# Final eligibility check
if is_active and eligible:
    print("Member is Eligible!")
else:
    print("Member is Not Eligible!")
