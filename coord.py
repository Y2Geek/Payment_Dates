"""A class to allow communication between the GUI and the core system"""
import copy

from account import Account
from payment import *
import data_handler

class Coord:
    
    def __init__(self):
        """Set up required lists"""
        self.accounts = data_handler.get_accounts()
        self.payments = data_handler.get_payments()

    # Account Related
    def create_account(self, data):
        """Creates and saves new accounts to acc.txt"""
        acc = data_handler.create_account(data)
        
        if acc:
            self.accounts.append(acc)
            data_handler.save_accounts(self.accounts)
            
            # Let the user know all was successful 
            return True


    def get_accounts(self):
        """Returns a list of known accounts"""
        return self.accounts


    def delete_account(self, index):
        """Deletes account from list and saves new list"""
        acc = self.accounts[index]
        self.accounts.remove(acc)
        data_handler.save_accounts(self.accounts)

        if acc in self.accounts:
            # delete failed, return False
            return False
        else:
            return True


    # Payment Related
    def create_payment(self, data):
        """Creates and saves the payment with the given information"""
        pay = data_handler.create_payment(data)
        # Add new payment to list
        if pay:
            self.payments.append(pay)
            data_handler.save_payments(self.payments)
            
            # Let the user know all was successful 
            return True


    def get_payments(self):
        """Returns a list of known payments"""
        return self.payments
    

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
        amount_in = 0.0
        amount_out = 0.0

        for acc in self.accounts:
            payments = acc.get_payments()

            if len(payments) > 0:
                # Print name of account, then payment details
                output.append(f"\n{acc.name}\n")

                # print short version of payment
                for pay in payments:
                    output.append(f"{pay.date.date()}\t{pay.name}\t{pay.value}")
                
                # Get balances
                balances = acc.get_balances()
                amount_in += balances[0]
                amount_out += balances[1]
        
        output.append(f"\n\nTotal income: {round(amount_in, 2)}\n"
                    + f"Total Outgoings: {round(amount_out, 2)}\n"
                    + f"Leaving: {round(amount_in - amount_out, 2)}")

        self.save_results(startdate, output)

        # Return output for display
        return output


    def save_results(self, startdate,  results):
        """Saves results t ofile, startdate as name for file"""
        data_handler.write_list_to_file(f"{startdate.date()}.txt", results)
