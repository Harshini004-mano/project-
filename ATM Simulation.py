# ATM Simulation with Visible PIN

# Initial balance
balance = 1000
# Set the correct PIN
correct_pin = "1234"

# Function to display menu
def show_menu():
    print("\nWelcome to the ATM Simulation")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")

# Function to validate PIN
def validate_pin():
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ").strip()  # Visible input
        if entered_pin == correct_pin:
            print("PIN is valid. Access granted.")
            return True
        else:
            attempts -= 1
            print(f"PIN is invalid. {attempts} attempt(s) remaining.")
    print("Too many incorrect attempts. Exiting program.")
    return False

# Start program
if validate_pin():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print(f"Your current balance is: ${balance}")
        elif choice == "2":
            amount = input("Enter amount to deposit: $").strip()
            if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
                balance += float(amount)
                print(f"${amount} deposited successfully. New balance: ${balance}")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif choice == "3":
            amount = input("Enter amount to withdraw: $").strip()
            if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
                if float(amount) <= balance:
                    balance -= float(amount)
                    print(f"${amount} withdrawn successfully. New balance: ${balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")
