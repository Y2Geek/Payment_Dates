from datetime import datetime as dt
import re

from account import Account
from payment import *
from coord import Coord


def print_list(items):
    """Prints the index and str of given items"""

    index = 0
    for item in items:
        print(f"{index}\t{str(item)}")
        index += 1


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
    
    # UPDATE REQUIRED 
    # Add sub optoins for account and payment
    selection = input(
        "\n\nWelcome!"
        "\nThis app will help you rememeber when your payments are due!"
        "\n\nPlease choose one of the following options:"
        "\n\n 1) Create/Delete an account"
        "\n 2) Create/Edit/elete a payment"
        "\n 3) Check what payments are due"
        "\n 4) Exit\n\n")
        
    if selection == '1':
        # Create/Delete a new account

        selection = input("\nWould you like to:"
        "\n 1) Create an account"
        "\n 2) Delete an existing Account"
        "\n 3) Return to the main menu: ")

        if selection == '1':
            # Create a new account
            
            name = input("\n\n Okay, what would you like to call this"
            "new account? ")
    
            if coord.create_account(name):
                print("\nYour account {name} has been added")
            else:
                print("There was a problem creating this account")
            
            continue
        elif selection == '2':
            # Delete an existing account
            accounts = coord.get_accounts()
            print_list(accounts)
            
            # Ask user for index of account to remove
            selection = input("Which account number would you like to delete? ")

            # Check input is within indexes
            pattern = re.compile(r"^\d+$")

            if pattern.match(selection):
                # Convert slection to int
                selection = int(selection)

                if selection >= 0 and selection <= len(accounts) - 1:
                    acc = accounts[selection]
                    successful = coord.delete_account(acc)

                    if successful:
                        print(f"Your account {str(acc)} has been deleted")
            
            else:
                print("Not a valid option")
            
            continue
        else:
            # If selection = 3 or other value return to main menu
            continue
    elif selection == '2':
        # Create/Edit/Delete a payment
        
        # IN PROGRESS

        break
    elif selection == '3':
        # Check payments due
        
        # Rewrite required 

        start_date = input("Please enter first date: (YYYY-MM-DD) ")
        end_date = input("Please enter first date: (YYYY-MM-DD) ")
        
        # Convert input into dates:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        
        # Get payments and output
        bills_due(start_date, end_date)
        output = get_output()
        
        # print and save output
        for line in output:
            print(line)
        File_Manager.write_to_file(output, f'{start_date.date()}.txt', False)
        
    elif selection == '4':
        # Exit
        break

