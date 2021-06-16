from datetime import datetime as dt

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


# Global variable
coord = Coord()

# Welcome the user
print("Welcome\n")

while True:
    # Repeat until user exits
    # Show a menu for the user to choose from
    print("> Main Menu <\n\nPlease choose from one of the following")

    # Show the menu options and wait for user to choose
    option = input(
        "1) Account Menu\n"
        "2) Payment Menu\n"
        "3) Upcoming Payment Check\n"
        "4) Exit\n\n")

    if option == '1':
        # Go to Account Menu
        continue
    elif option == '2':
        # Go to Payment Menu
        continue
    elif option == 3:
        # Go to Upcoming Payment Check method
        continue
    elif option == '4':
        print("\nHave an amazing day\nExiting. . . ")
        break
    else:
        print(f"\n (!) Sorry {option} is not a valid option, please try again\n")
        continue