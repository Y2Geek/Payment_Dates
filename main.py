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


def get_account():
    """Shows the user known accounts and returns selected one"""
    print_accounts()
    index = input("\nWhich number would you like to remove? ")

    if data_handler.valid_int(index):
        index = int(index)
        
        if index >= 0 and index < number_of_accounts():
            return coord.accounts[index]


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
    acc = get_account()

    if acc:
        confirm = input(f"Are you sure you want to remove {acc.name}? (Y or N)\n"
                "Deleting an account can cause errors if payments use it: ")

        if confirm.lower() == 'y':
            successful = coord.delete_account(acc)

            if successful:
                print("Account deleted")
            else:
                print("Cannot remove account")
        else:
            print("Okay, No changes made")
    else:
        # Not a valid index
        print("Not a valid input")


def print_accounts():
    """Prints a list of accounts with index numbers"""
    accounts = coord.get_accounts()
    print_list(accounts)


# Payment Menu Options
def get_payment_type():
    """Asks the user if this is an IN or OUT payment, returns result"""
    selection = input("Is this a\n"
            "1) Payment in\n"
            "2) Payment out? ")
    
    if selection == '1':
        return 'IN'
    elif selection == '2':
        return 'OUT'
    else:
        return None


def get_value():
    """Asks the user for the value of a payment and returns it as a float"""
    return data_handler.valid_amount(input("Please enter the value of this payment (No commas please): "))


def get_frequency():
    """Lets the user choose the frequency for a payment"""
    selection = input("How frequently is this payment made?\n"
            "1) Daily\n"
            "2) Weekly\n"
            "3) Fortnightly\n"
            "4) Four Weekly\n"
            "5) Monthly"
            "6) Quarterly\n"
            "7) Half Yearly\n"
            "8) Yearly: ")
        
    if input == '1':
        return input
    elif input == '2':
        return input
    elif input == '3':
        return input
    elif input == '4':
        return input
    elif input == '5':
        return input
    elif input == '6':
        return input
    elif input == '7':
        return input
    elif input == '8':
        return input
    else:
        return None


def create_payment():
    """Takes input from user to create a payment"""
    acc = get_account()
    pay_type = get_payment_type()
    date = get_date()
    name = input("Please enter a name for this payment: ")
    value = get_value()

    # check if this is an ongoing payment
    ongoing = input("Is this an ongoing payment? (Y or N) ")
    
    if ongoing.lower() == 'y':
        frequency = get_frequency()
        coord.create_payment(acc, pay_type, date, name, value, frequency)
    else:
        coord.create_payment(acc, pay_type, date, name, value)


def view_all_payments():
    """Prints a list of all known payments"""
    payments = coord.get_payments()
    
    if payments:
        # If there are payments, list them
        print("\nHere are all known payments\n")
        print_list(payments)
    else:
        # Let the user know there are no payments to display
        print("\nYou don't currently have any payments")


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
        while True:
            print("\n> Payment Menu <\n\nPlease choose from one of the following options:")

            option = input(
                "1) Add New Payment\n"
                "2) Delete Existing Payment\n"
                "3) View All Known Payments\n"
                "4) Main Menu\n\n")

            if option == '1':
                # Create Payment
                create_payment()
                continue
            elif option == '2':
                # Delete Payment
                continue
            elif option == '3':
                view_all_payments()
                continue
            else:
                break

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