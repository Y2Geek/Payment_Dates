"""A collection of methods related to loading, creating and saving object states"""

import os
from account import Account

# File related methods
def get_data(file_path):
    """
    Returns the contents of the given file, with each line stripped
    Returns None if file was not found
    """

    # Check if file exists
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.readlines()
            
            # Remove whitespace from start and end of line
            contents = []
            for line in lines:
                line = line.strip()
                
                # Ignore blank lines
                if len(line) > 0:
                    contents.append(line)
                else:
                    continue
            
        return contents
    else:
        # Return empty list if file not found
        return []


def write_list_to_file(file_path, contents):
    """Writes given contents to the given file"""
    with open(file_path) as f:
        for line in contents:
            # Write the string reprresentation to given file
            f.write(f"{str(line)}\n")


# Account related methods
account_file = f"Config{os.sep}Acc.txt"

def get_accounts():
    """Creates a list of accounts based on data from Acc.txt"""
    
    # Create empty list to hold accounts
    accounts = []
    # Get account data
    data = get_data(account_file)

    # if data, create accounts
    if data:
        for acc in data:
            accounts.append(create_account(acc))

    return accounts


def create_account(data):
    """Creates and returns an account with given data"""
    return Account(data)


def save_accounts(account_list):
    """Saves given list of accounts, to Acc.txt"""
    write_list_to_file(account_file, account_list)


# Payment related methods
payment_file = f"Config{os.sep}AllPayments.txt"

def get_payments():
    """Creates a list of payments based on data from AllPayments.txt"""
    
    # Create empty list to hold payments
    payments = []
    # Get payment data
    data = get_data(payment_file)

    # if data, create payments
    if data:
        for pay in data:
            payments.append(create_payment(pay))

    return payments


def create_payment(data):
    """Creates and returns a payment with given data"""
    #TO BE IMPLEMENTED


def save_payments(payment_list):
    """Saves given list of payments, to AllPayments.txt"""
    write_list_to_file(payment_file, payment_list)