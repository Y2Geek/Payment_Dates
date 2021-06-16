"""A class to allow communication between the GUI and the core system"""

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


    def delete_account(self, acc):
        """Deletes account from list and saves new list"""
        self.accounts.remove(acc)
        data_handler.save_accounts(self.accounts)

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