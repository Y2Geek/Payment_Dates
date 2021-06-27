"""A class to allow communication between the GUI and the core system"""
import os
import copy

from account import Account
from payment import *
import data_handler

class Coord:
    
    def __init__(self):
        """Set up required lists"""
        self.accounts = []
        self.payments = []
        self._account_file = f"Config{os.sep}Acc.txt"
        self._payment_file = f"Config{os.sep}AllPayments.txt"
        self.get_data()


    def get_data(self):
        """Get data from config files, and put them in lists"""
        self._get_accounts()
        self._get_payments()
        print(len(self.accounts), len(self.payments))


    # Account Related
    def create_account(self, data):
        """Creates and saves new accounts to acc.txt"""
        self.accounts.append(Account(data))
        
        # Let the user know all was successful 
        return True


    def _get_accounts(self):
        """Creates a list of accounts based on data from Acc.txt"""
    
        # Get account data
        data = data_handler.get_data(self._account_file)

        # if data, create accounts
        if data:
            for acc in data:
                self.create_account(acc)


    def get_accounts(self):
        """Returns a list of known accounts"""
        return self.accounts


    def delete_account(self, acc):
        """Deletes account from list and saves new list"""
        self.accounts.remove(acc)
        self.save_accounts()

        if acc in self.accounts:
            # delete failed, return False
            return False
        else:
            return True


    def save_accounts(self):
        """Saves account list of accounts, to Acc.txt"""
        data_handler.write_list_to_file(self._account_file, self.accounts)


    # Payment Related
    def create_payment(self, data):
        """Creates payment with the given information"""
        
        # Check data and convert where needed
        data = data_handler.validate_data(data, self.accounts)

        # Data will be None if any errors 
        if data:
            # Check lenght of input_data, to see what type of payment to create
            if len(data) == 5:
                # Create one time payment
                self.payments.append(Payment(data[0], data[1], data[2], data[3], data[4]))
            elif len(data) == 6:
                self.payments.append(Ongoing_Payment(data[0], data[1], data[2], data[3], data[4], data[5]))
        else:
            # If anything went wrong with validation raise error
            raise ValueError(f"Was unable to validate payment {data}")


    def _get_payments(self):
        """Creates a list of payments based on data from AllPayments.txt"""
    
        # Get payment data
        data = data_handler.get_data(self._payment_file)

        # if data, create payments
        if data:
            for pay in data:
                self.create_payment(pay)


    def get_payments(self):
        """Returns a list of known payments"""
        return self.payments
    

    def save_payments(self):
        """Saves payment list to AllPayments.txt"""
        data_handler.write_list_to_file(self._payment_file, self.payments)


    def update_payment_dates(self, startdate):
        """
        Returns a list of payments that have a date after start date.
        Moves payment dates forward if before start date and is ongoing payment
        """
        relevant_payments = []

        for pay in self.payments:
            if pay.date < startdate:
                # Check if ongoing payment
                if isinstance(pay, Ongoing_Payment):
                    while pay.date < startdate:
                        pay.next_date()
                    
                    relevant_payments.append(pay)
                else:
                    # Ignore outdated one off payments
                    continue
            else:
                relevant_payments.append(pay)
        
        return relevant_payments


    def get_payments_between(self, startdate, enddate):
        """Returns payments between given dates"""

        # Make sure all payments are equal or after startdate
        payments = self.update_payment_dates(startdate)

        relevant_payments = []

        # Check for payments that are between startdate and enddate
        for pay in payments:
            if pay.date >= startdate and pay.date < enddate:
                relevant_payments.append(pay)

                # Check if payment needs to be added more than once
                if isinstance(pay, Ongoing_Payment):
                    pay1 = copy.copy(pay)
                    while pay1.date < enddate:
                        pay1.next_date()
                        if pay1.date < enddate:
                            relevant_payments.append(pay1)
        
        return relevant_payments


    def split_account_payments(self, payments):
        """Puts each payment into the connected account"""
        for pay in payments:
            pay.account.add_payment(pay)


    def get_output(self, startdate):
        """Returns a list to be displayed and saved"""
        
        output = []
        amount_in = 0
        amount_out = 0

        for acc in self.accounts:
            payments = acc.get_payments()

            if len(payments) > 0:
                # Print name of account, then payment details
                output.append(f"{acc.name}\n")

                # print short version of payment
                for pay in payments:
                    output.append(f"{pay.date.date()}\t{pay.name}\t{pay.get_fvalue()}")

                # add extra blank line in output
                output.append("\n")

                # Get balances
                balances = acc.get_balances()
                amount_in += balances[0]
                amount_out += balances[1]

            # Clear account payments
            acc.payments.clear()

        # Convert amount_in and amount_out in to floats
        amount_in = float(amount_in / 100)
        amount_out = float(amount_out / 100)

        output.append(f"Total income: {amount_in}\n"
                    + f"Total Outgoings: {amount_out}\n"
                    + f"Leaving: {round(amount_in - amount_out, 2)}")

        self.save_results(startdate, output)

        # Return output for display
        return output


    def save_results(self, startdate,  results):
        """Saves results t ofile, startdate as name for file"""
        data_handler.write_list_to_file(f"{startdate.date()}.txt", results)
