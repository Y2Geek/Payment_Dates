from datetime import date
from datetime import timedelta
from account import Account
import add_months

"""Classes representing different types of payment"""

class Payment:
    """A class representing a basic one time payment"""
    
    def __init__(self, account, payment_type, date, name, value):
        """Initialize attributes"""
        self.account = account # Account object
        self.payment_type = payment_type # IN/OUT
        self.date = date # datetime object
        self.name = name
        self.value = value
    
    def __lt__(self, other):
        """Compare attributes of this payment to other, for sorting"""
        if self.date == other.date:
            # If date are same, is one an IN payment?
            # If so have that listed first
            return self.payment_type < other.payment_type
        else:
            # Base order on date and name
            return self.date < other.date
    
    def __str__(self):
        """Returns a String representing the current state"""
        details = f"{self.account.name}\t{self.payment_type}\t{self.date.date()}\t{self.name}\t{self.value}"
        return details


class Ongoing_Payment(Payment):
    """A class representing a payment with no end date"""

    def __init__(self, account, payment_type, date, name, value, period):
        """Initialize parent and then own attributes"""
        super().__init__(account, payment_type, date, name, value)
        self.period = period # DAILY, WEEKLY, FORTNIGHTLY, 
        # FOURWEEKLY, MONTHLY, QUATERLY, HALFYEARLY, YEARLY
    
    def next_date(self):
        """Moves date forward by slef.frequency * self.period"""
        
        if self.period == 'DAILY':
            self.date = self.date + timedelta(days=1)
        elif self.period == 'WEEKLY':
            self.date = self.date + timedelta(weeks=1)
        elif self.period == 'FORTNIGHTLY':
            self.date = self.date + timedelta(weeks=2)
        elif self.period == 'FOURWEEKLY':
            self.date = self.date + timedelta(weeks=+4)
        elif self.period == 'MONTHLY':
            self.date = add_months.add_months(self.date, 1)
        elif self.period == 'QUARTERLY':
            self.date = add_months.add_months(self.date, 3)
        elif self.period == 'YEARLY':
            self.date = add_months.add_months(self.date, 12)
        else:
            print("***** MISSED *****")
            print(f"{self.full_details()}")
            print(f"got {self.period}")
    
    def __str__(self):
        """Returns a String representing the current state"""
        
        details = str(super)
        details = f"{details}\t{self.period}"
        return details
