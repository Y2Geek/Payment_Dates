from datetime import datetime

def days_in_month(month, year):
    """ Returns the number of days in the given month"""
    
    # Check if month is valid
    if month >= 1 and month <= 12:
        # create list of months that have 31 days
        long_months = [1, 3, 5, 7, 8, 10, 12]

        # Return the number of months in the given month
        if month == 2:
            # If month is February, check if year is a leap year
            if year % 4 == 0:
                return 29
            else:
                return 28
        elif month in long_months:
            # Return 31 if given month appears in above list
            return 31
        else:
            # Return 30 days as not caught above
            return 30


def get_new_month(date, num_of_months):
    """
    Adds month to date.  If new month is in the next year, returns the 
    new year too.  Otherwise returns new month with existing year.
    """
    if num_of_months >= 1 and num_of_months < 12:
        new_month = date.month + num_of_months

        if new_month > 12:
            new_month -= 12
            new_year = date.year +1
            return (new_month, new_year)
        elif new_month <= 12:
            return (new_month, date.year)
    elif num_of_months == 12:
        # Return original month with new year
        new_year = date.year +1
        return (date.month, new_year)


def add_months(date, num_of_months):
    """Moves date forward by given number of months"""
    
    if num_of_months < 1 or num_of_months > 12:
        return None
    
    new_details = get_new_month(date, num_of_months)

    # Check number of days in given month
    days_in_new_month = days_in_month(new_details[0], new_details[1])

    if date.day > days_in_new_month:
        day = days_in_new_month
    else:
        day = date.day
    
    # new_details[1] is year
    # new_details[0] is month
    return datetime(new_details[1], new_details[0], day)
