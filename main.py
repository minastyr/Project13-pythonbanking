"""This function handles the transfer process for the user."""
# TODO: Import the Checking, Savings, and Validation classes
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation

# TODO: Import the handle_deposit, handle_withdrawal, handle_transfer, and balances functions
from BankingFunctions.deposit import handle_deposit
from BankingFunctions.withdraw import handle_withdrawal
from BankingFunctions.transfer import handle_transfer, balances

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
           "contain at least one uppercase and lowercase letter,\n"
           "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # Initialize the attempts variable to 1
    attempts = 1
    # Create a while loop to validate the email and password
    while attempts < 3:
        # Validate the email and password using the Validation class
        if Validation.validate_email(email) and Validation.validate_password(password):
            # If valid, break out of the loop
            break
        else:
            # If invalid, prompt the user again and increment attempts
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            attempts += 1

    # If maximum number of attempts is reached, print a message and exit
    if attempts == 3:
        print("Maximum login attempts reached. Exiting program.")
        return

    # Set up accounts with default balances.
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # Print a message for the user inform them of their checking and savings balances
    print("Here are your account balances:")
    print(f"Checking: ${checking_account.get_balance():,.2f}")
    print(f"Savings: ${savings_account.get_balance():,.2f}")

    # Present a menu of options to the user
    while True:
        print("\nWhat would you like to do?")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. Make a transfer")
        print("4. Check account balances")
        print("q. Quit")
        
        # Get user's choice
        choice = input("Enter your choice (1, 2, 3, 4, or q): ")
        
        # Create a list of valid choices
        valid_choices = ['1', '2', '3', '4', 'q']
        
        if choice in valid_choices:
            if choice == '1':
                # Call the handle_deposit function
                handle_deposit(checking_account, savings_account)
            elif choice == '2':
                # Call the handle_withdrawal function
                handle_withdrawal(checking_account, savings_account)
            elif choice == '3':
                # Call the handle_transfer function
                handle_transfer(checking_account, savings_account)
            elif choice == '4':
                # Call the balances function
                balances(checking_account, savings_account)
            elif choice == 'q':
                # Exit the program
                print("Thank you for using our banking system. Goodbye!")
                break
        else:
            # If user enters invalid choice, print a message
            print("Invalid choice. Please enter 1, 2, 3, 4, or q.")

if __name__ == "__main__":
    main()
