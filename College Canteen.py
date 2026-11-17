
# Prepaid College Canteen Card System

balance = 500
correct_pin = 4321
attempts = 3

# PIN Verification
while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN! Attempts left:", attempts)

if attempts == 0:
    print("Your Card is Blocked!")

else:
    while True:
        print("\n--- Canteen Menu ---")
        print("1. Check Balance")
        print("2. Recharge")
        print("3. Make Purchase")
        print("4. View Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter recharge amount: "))

            if amount <= 0:
                print("Invalid Amount!")
                continue

            balance += amount
            print("Recharge Successful!")

        elif choice == 3:
            amount = int(input("Enter purchase amount: "))

            if amount <= 0:
                print("Invalid Amount!")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Purchase Successful!")

        elif choice == 4:
            pass

        elif choice == 5:
            print("Final Balance:", balance)
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")
