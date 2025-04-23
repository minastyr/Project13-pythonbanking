"""This function handles the withdrawal process for the user."""

# Pass in the checking_account and savings_account objects.
def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.

    The function prompts the user to select an account and make a withdrawal.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After each withdrawal, the function prints the updated balance of the respective account.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to make a withdrawal?")
    print("1. Checking")
    print("2. Savings")
    print("q. Return to main menu")
    # Prompt the user to select an account to make a withdrawal.
    account_choice = input("Enter your choice (1, 2, or q): ")
    # If the user chooses to quit, return from the function.
    if account_choice.lower() == 'q':
        return

    try:
        # If the selection is in a list of valid choices, i.e ['1', '2']
        if account_choice in ['1', '2']:
            try:
                # Prompt the user to enter the amount to withdraw and convert it to a float.
                amount = float(input("Enter the amount to withdraw: $"))

            # Use the ValueError as an exception.
            except ValueError:
                # Print an error message if the user enters an invalid amount.
                print("Please enter a dollar amount.")

                # Call the handle_withdrawal function recursively for an invalid amount.
                handle_withdrawal(checking, savings)

                # Ensure the function returns after the recursive call.
                return

            # Add an if/else conditional statement to check the account choice,
            if account_choice == '1':
                try:
                    # Call the withdraw method on the appropriate account.
                    checking.withdraw(amount)
                    # Add a print statement to display the updated balance after the withdrawal
                    # Format the balance to two decimal places and thousands.
                    print(f"Withdrawal successful. Your checking account balance is now ${checking.get_balance():,.2f}")
                except ValueError as e:
                    print(e)
                    return handle_withdrawal(checking, savings)
            else:
                try:
                    # Call the withdraw method on the appropriate account.
                    savings.withdraw(amount)
                    # Add a print statement to display the updated balance after the withdrawal
                    # Format the balance to two decimal places and thousands.
                    print(f"Withdrawal successful. Your savings account balance is now ${savings.get_balance():,.2f}")
                except ValueError as e:
                    print(e)
                    return handle_withdrawal(checking, savings)
        else:
            # Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please enter 1, 2, or q.")
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_withdrawal(checking, savings)
