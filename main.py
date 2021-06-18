from datetime import datetime as dt
import copy
from datetime import datetime

from account import Account
from payment import *
from coord import Coord
import data_handler


# Common methods
def number_of_accounts():
    """Returns an int representing the number of accounts known"""
    return len(coord.get_accounts())


def number_of_payments():
    """Returns an int representing the number of known payments"""
    return len(coord.get_payments())


def print_list(list):
    """Print the given list, with index numbers"""
    index = 0

    for item in list:
        # Print index with item string
        print(f"{index}\t{str(item)}")
        index += 1


def get_date(date_type):
    """Asks the user to enter a date, repeats until valid date given"""
    date = None
    while not date:
        input_date = input(f"Please enter a {date_type} in the form YYYY-MM-DD: ")
        if data_handler.valid_date(input_date):
            date = datetime.strptime(input_date, '%Y-%m-%d')
            return date


# Account Menu Options
def create_account():
    """Asks the user for information to set up account"""

    name = input("What would you like to call this account? ")
    successful = coord.create_account(name)

    if successful:
        coord.save_accounts()
        print(f"Your {name} account has been set up!\n")
    else:
        print(f"Was unable to set up account {name}, you may have an account\n"
            "with this name already\n")


def delete_account():
    """Asks user to choose an account to remove"""
    print_accounts()
    index = input("\nWhich number would you like to remove? ")

    if data_handler.valid_int(index):
        index = int(index)
        
        if index >= 0 and index < number_of_accounts():
            confirm = input(f"Are you sure you want to remove {coord.accounts[index].name}? (Y or N)\n"
                "Deleting an account can cause errors if payments use it: ")

            if confirm.lower() == 'y':
                successful = coord.delete_account(index)

                if successful:
                    print("Account deleted")
                else:
                    print("Cannot remove account")
            else:
                print("Okay, No changes made")
        else:
            # Not a valid index
            print("Not a valid input")
    else:
        # Not a valid index
        print("Not a valid input")


def print_accounts():
    """Prints a list of accounts with index numbers"""
    accounts = coord.get_accounts()
    print_list(accounts)


# Payment Menu Options



# Upcoming Payment Check Menu Option

def print_account_payments(startdate):
    """Prints output of relevant payments"""

    output = coord.get_output(startdate)
    if len(output) > 0:
        for line in output:
            print(line)

    
def upcoming_payments():
    """Asks the user for two dates, and returns a list of payments in those dates"""
    
    # Make sure there are known payments
    if number_of_payments() > 0:
        startdate = get_date('start date')
        
        # Make usre end date is after start date
        enddate = datetime.min
        if enddate <= startdate:
            enddate = get_date('end_date')

        # Find relevant payments
        payments = coord.get_payments_between(startdate, enddate)

        # split payments and display on screen
        coord.split_account_payments(payments)
        print_account_payments(startdate)


# Global variable
coord = Coord()

# Greet the user
print("Welcome\n")

while True:
    # Repeat until user exits
    # Show a menu for the user to choose from
    print("\n> Main Menu <\n\nPlease choose from one of the following options:")

    # Show the menu options and wait for user to choose
    option = input(
        "1) Account Menu\n"
        "2) Payment Menu\n"
        "3) Upcoming Payment Check\n"
        "4) Exit\n\n")

    if option == '1':
        # Account Menu optoins
        while True:
            print("\n> Account Menu <\n\nPlease choose from one of the following options:")

            option = input(
            "1) Add New Account\n"
            "2) Delete Existing Account\n"
            "3) View Accounts\n"
            "4) Main Menu\n\n")

            if option == '1':
                # Create Account
                create_account()
                continue
            elif option == '2':
                # Delete Account
                delete_account()
                continue
            elif option == '3':
                # View accounts
                print_accounts()
                continue
            elif option == '4':
                break

    elif option == '2':
        # Payment Menu optoins
        print("\n> Payment Menu <\n\nPlease choose from one of the following options:")
        continue
    elif option == '3':
        # Upcoming payment check
        upcoming_payments()
        continue
    elif option == '4':
        print("\nHave an amazing day\nExiting. . . ")
        break
    else:
        print(f"\n (!) Sorry {option} is not a valid option, please try again\n")
        continue