import time

print("Please insert your card")
time.sleep(5)

password = 12345
pin = int(input("Please enter your ATM PIN: "))
balance = 5000

if pin == password:
    while True:
        print("""
             1 == Check Balance
             2 == Withdraw
             3 == Deposit
             4 == Exit
             """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("=====================================================")
            print("=====================================================")
            print("=====================================================")
        elif option == 2:
            withdraw_amount = int(input("Please enter the amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} has been debited from your account")
                print("=====================================================")
                print("=====================================================")
                print(f"Your current balance is {balance}")
                print("=====================================================")
                print("=====================================================")
        elif option == 3:
            deposit_amount = int(input("Please enter the amount to deposit: "))
            print("=====================================================")
            balance += deposit_amount
            print(f"{deposit_amount} has been credited to your account")
            print("=====================================================")
            print("=====================================================")
            print(f"Your current balance is {balance}")
            print("=====================================================")
            print("=====================================================")
        elif option == 4:
            print("Thank you for using our ATM. Please visit again.")
            break
        else:
            print("Invalid option. Please try again")
else:
    print("Wrong PIN. Please try again later.")
