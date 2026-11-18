# Practical No. 2 – Flow Control
# Simple ATM Program

balance = 10000
correct_pin = 1234
attempts = 3

# PIN Verification
while attempts > 0:
    pin = int(input("Enter your ATM PIN: "))

    if pin == correct_pin:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN! Attempts left:", attempts)

if attempts == 0:
    print("Your ATM is Locked!")

else:
    # ATM Menu
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount < 0:
                print("Negative amount not allowed!")
                continue
            else:
                balance += amount
                print("Amount Deposited Successfully!")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount < 0:
                print("Negative amount not allowed!")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Please collect your cash.")

        elif choice == "4":
            pass

        elif choice == "5":
            print("Thank you for using ATM!")
            print("Final Balance:", balance)
            break

        else:
            print("Invalid Choice!")

