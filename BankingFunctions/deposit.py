"""This function handles the deposit process for the user."""

# Build out the handle_deposit function
# Pass in the checking account and savings account objects.
def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    print("1. Checking")
    print("2. Savings")
    print("q. Return to main menu")
    # Prompt the user to select an account and make a deposit.
    account_choice = input("Enter your choice (1, 2, or q): ")
    # If the user chooses to quit, return from the function.
    if account_choice.lower() == 'q':
        return

    try:
        # If the selection is in a list of valid choices, i.e ['1', '2']
        if account_choice in ['1', '2']:
            try:
                # Prompt the user to enter the amount to deposit and convert it to a float.
                amount = float(input("Enter the amount to deposit: $"))

            # Use the ValueError as an exception.
            except ValueError:
                # Print an error message if the user enters an invalid amount.
                print("Please enter a dollar amount.")

                # Call the handle_deposit function recursively for an invalid amount.
                handle_deposit(checking, savings)

                # Ensure the function returns after the recursive call.
                return

            # Add an if/else conditional statement to check the account choice,
            if account_choice == '1':
                # Call the deposit method on the appropriate account.
                checking.deposit(amount)
                # Add a print statement to display the updated balance after the deposit
                # Format the balance to two decimal places and thousands.
                print(f"Deposit successful. Your checking account balance is now ${checking.get_balance():,.2f}")
            else:
                # Call the deposit methods on the appropriate account.
                savings.deposit(amount)
                # Add a print statement to display the updated balance after the deposit
                # Format the balance to two decimal places and thousands.
                print(f"Deposit successful. Your savings account balance is now ${savings.get_balance():,.2f}")
        else:
            # Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please enter 1, 2, or q.")
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
