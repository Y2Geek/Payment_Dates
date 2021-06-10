class Account:
    """Class that represents a basic bank account"""
    
    def __init__(self, name):
        """Initialize object attributes"""
        self.name = name
        self.payments = [] # Payment objects to be added during execution
    

    def add_payment(self, payment):
        """Add given payment to payments list"""
        self.payments.append(payment)
    

    def get_balances(self):
        """Returns the total amount in/out and incomes - outgoings"""
        
        if len(self.payments) != 0:
            # If payments is not empty, calcualte totals

            # Create holding variables for totals
            total_in = 0.0
            total_out = 0.0
            
            for payment in self.payments:
                if payment.payment_type == 'IN':
                    total_in += payment.value
                else:
                    total_out += payment.value
                
        # Return tuple with totals
        return (total_in, total_out)
    

    def clear_payments(self):
        """Method to clear the payments variable of self"""
        self.payments = []


    def __str__(self):
        return f'{self.name}'
