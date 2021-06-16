from datetime import datetime as dt
from io import DEFAULT_BUFFER_SIZE
import re

from account import Account
from payment import *
from coord import Coord
import data_handler


def print_list(items):
    """Prints the index and str of given items"""

    index = 0
    for item in items:
        print(f"{index}\t{str(item)}")
        index += 1


# Account Menu Optoins
def create_account():
    """Menu optoin for create account"""
    name = input("\n\n Okay, what would you like to call this"
            "new account? ")
    
    if coord.create_account(name):
        print("\nYour account {name} has been created")
    else:
        print("There was a problem creating this account")


def delete_account():
    """Menu option for delete account"""
    
    # Get a list of accounts, and output them to console
    accounts = coord.get_accounts()
    
    # check that list is not empty
    if accounts:
        print_list(accounts)

        # Ask user for index of account to remove
        selection = input("Which account number would you like to remove? ")

        # Convert selection to an int
        selection = data_handler.valid_int(selection)

        # Check selectoin doesn't equal None
        if selection:
            if selection >= 0 and selection <= len(accounts) - 1:
                acc = accounts[selection]
                    
                # Warn user about deleting account
                delete = input(f"You have chosen to delete {acc.name} are you sure you "
                            "want to do this?\nDeleting an account that is connected to a payment"
                            " can cause errors (Y or N): ")

                if delete.lower() == 'y':
                    successful = coord.delete_account(acc)
                        
                    if successful:
                        print(f"Your account {str(acc)} has been deleted")
                    else:
                        print("Was unable to dlete account")
                else:
                        # If user chooses not to delete account
                        print("\nYour account has not been removed")
            else:
                print("Not a valid option")
    
    else:
        print("You don't have any accounts yet")
    
    return


def create_payment():
    # Code to be added shortly
    return


def get_output():
    """Gather information to be printed and/or saved """
    
    output = []
    balances = ()
    bal_in = 0.0
    bal_out = 0.0
    
    # Rewrite in progress

    """for account in a_manager.accounts:
        if account.payments:
            output.append(f"{account.name} \n")
            account.payments.sort()
            for payment in account.payments:
                output.append(f'{payment.date.date()}\t{payment.name}\t{payment.value}')
            
            # Add a blank line to output
            output.append("\n")
            
            balances = account.get_balances()
            bal_in += balances[0]
            bal_out += balances[1]
        
        # Clear account payments
        account.clear_payments()
        
    output.append(f"income: £{round(bal_in, 2)}"
    f"\noutgoings: £{round(bal_out, 2)}"
    f"\nleft: £{round(bal_in - bal_out, 2)}")
    
    return output"""

coord = Coord()

while True:
    selection = input(
        "\n\nWelcome!"
        "\nThis app will help you rememeber when your payments are due!"
        "\n\nPlease choose one of the following options:"
        "\n\n 1) Create/Delete an account"
        "\n 2) Create/Edit/elete a payment"
        "\n 3) Check what payments are due"
        "\n 4) Exit\n\n")
        
    if selection == '1':
        # Create/Delete an account

        selection = input("\nWould you like to:"
        "\n 1) Create a new account"
        "\n 2) Delete an existing account"
        "\n 3) Return to the main menu: ")

        if selection == '1':
            # Create a new account
            create_account()
            continue
        elif selection == '2':
            # Delete an existing account
            delete_account()
            continue
        else:
            # If selection = 3 or other value return to main menu
            continue
    elif selection == '2':
        # Create/Edit/Delete a payment
        
        selection = input("\nWould you like to:"
        "\n 1) Create a new payment"
        "\n 2) Delete an existing payment"
        "\n 3) Edit an existing payment"
        "\n 4) Return to main menu")

        # In Progress
        continue
    