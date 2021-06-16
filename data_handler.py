"""A collection of methods related to loading, creating and saving object states"""

import re
import os
from datetime import datetime
from account import Account
from payment import Payment, Ongoing_Payment

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
    with open(file_path, 'w') as f:
        for line in contents:
            # Write the string reprresentation to given file
            f.write(f"{str(line)}\n")


# Account related methods
account_file = f"Config{os.sep}Acc.txt"
accounts = []

def get_accounts():
    """Creates a list of accounts based on data from Acc.txt"""
    
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


def get_account(name):
    """Returns account from accounts with given name, return None if nott found"""
    for acc in accounts:
        if acc.name == name:
            return acc
    
    # If no account found, return None
    return None


def save_accounts(account_list):
    """Saves given list of accounts, to Acc.txt"""
    write_list_to_file(account_file, account_list)


# Payment related methods
payment_file = f"Config{os.sep}AllPayments.txt"
payments = []

def get_payments():
    """Creates a list of payments based on data from AllPayments.txt"""
    
    # Get payment data
    data = get_data(payment_file)

    # if data, create payments
    if data:
        for pay in data:
            create_payment(pay)

    return payments


def create_payment(input_data):
    """Creates and adds a payment with given data to payments"""
    data = validate_data(input_data)

    if data:
        # Check lenght of input_data, to see what type of payment to create
        if len(data) == 5:
            # Create one time payment
            return Payment(data[0], data[1], data[2], data[3], data[4])
        elif len(data) == 6:
            return Ongoing_Payment(data[0], data[1], data[2], data[3], data[4], data[5])
    else:
        # If anything went wrong with validation raise error
        raise ValueError(f"Was unable to validate payment {input_data}")


def save_payments(payment_list):
    """Saves given list of payments, to AllPayments.txt"""
    write_list_to_file(payment_file, payment_list)


# Input Validation
def valid_date(input):
    """Checks if input is a valid date and returns a dateteim object"""
    
    # Date should be in format dddd-mm-dd
    format = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    if format.match(input):
        # Try convert input into a date
        try:
            date = datetime.strptime(input, '%Y-%m-%d')
        except:
            # If any error occours, return None
            return None
        else:
            return date
    else:
        # If format does not match, return None
        return None


def valid_amount(input):
    """Checks if valid amount entered, and returns float if true"""
    
    # Input must be only digits and decimal with a maximum
    # 2 decimal places.
    format = re.compile(r"^\d+.\d{0,2}$")

    if format.match(input):
        # If input matches format, convert to decimal
        return float(input)
    else:
        # If not a valid value, return None
        return None


def valid_payment_type(input):
    """Checks that input is either IN or OUT, and returns string in uppercase"""
    input = input.upper()

    if input.upper() == 'IN':
        return input
    elif input.upper() == 'OUT':
        return input
    else:
        return None


def validate_data(input_data):
    data = input_data.split('\t')

    # Check and convert all common data
    account = get_account(data[0])
    if not account:
        # If account not found, return None
        return None
    
    payment_type = valid_payment_type(data[1])
    if not payment_type:
        # If payment_type not valid, return None
        return None
    
    date = valid_date(data[2])
    if not date:
        # If date not valid, return None
        return None

    name = data[3]
    value = valid_amount(data[4])
    if not value:
        # If amount not valid, return None
        return None

    if len(data) == 5:
        return(account, payment_type, date, name, value)
    elif len(data) == 6:
        frequency = valid_frequency(data[5])

        if frequency:
            return(account, payment_type, date, name, value, frequency)
        else:
            return None


def valid_frequency(input):
    """Checks the input frequency is valid, return frequency if valid"""
    input = input.upper()

    if input == 'DAILY':
        return input
    elif input == 'WEEKLY':
        return input
    elif input == 'FORTNIGHTLY':
        return input
    elif input == 'FOURWEEKLY':
        return input
    elif input == 'MONTHLY':
        return input
    elif input == 'QUARTERLY':
        return input
    elif input == 'HALFYEARLY':
        return input
    elif input == 'YEARLY':
        return input
    else:
        return None


def valid_int(input):
    """Checks if input is an int.  Returns int if valid, None otherwise"""
    # Check input is within indexes
    pattern = re.compile(r"^\d+$")

    if pattern.match(input):
        # Return int
        return int(input)
    
    # If not valid, return None
    return None