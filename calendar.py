#
# This program find the day of the specified data
# My father has taught me to find day, which he learnt in his school days.

# Load all module
from datetime import date


# Day names where 0 means Sunday
vaar_names = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Odd days in a month
odd_days_in_month = (31 % 7, 28 % 7, 31 % 7, 30 % 7,
                     31 % 7, 30 % 7, 31 % 7, 31 % 7,
                     30 % 7, 31 % 7, 30 % 7, 31 % 7)

# Find full year
def find_fullyear(user_year):
    """ Full year: Years completed till that year """
    return user_year - 1

def find_leapyears_in_fullyear(fl_year):
    """
    Total number of leap years in full years starting from beginning of the 
    century 1900, 2000.
    """
    leap_years = fl_year % 100
    leap_years //= 4
    return (leap_years % 7)


def odd_days_in_century_years(fl_year):
    """
    Find odd days in century years
    100 years has 5 odd days
    200 years has 3 odd days
    300 years has 1 odd days
    """
    #    Leap years in a century: In a 100-year period, there are typically 24 leap years
    #    and 76 ordinary years. The 100th year itself is not a leap year unless it is
    #    divisible by 400 (e.g., 1600, 2000 are leap years, but 100, 200, 300 are not).
    #
    #    Total odd days in 100 years:Odd days from 76 ordinary years: 76 x 1=76 odd days.
    #    Odd days from 24 leap years: 24 x 2=48 odd days.
    #    Total odd days: 76 + 48 = 124 days
    #    124 / 7= 17 weeks and a remainder of 5 days.
    #    100 years has 5 odd days
    #    200 years has 3 odd days
    #    300 years has 1 odd days - 300 brabar ae 1
    centuries = fl_year % 1000
    if centuries >= 300:
        return 1
    elif centuries >= 200:
        return 3
    elif centuries >= 100:
        return 5
    else :
        return 0


def odd_days_in_full_year(fl_year):
    """ Number of odd days in full year """
    return (fl_year % 100) % 7

# +1 day for february month
def is_current_leapyear(usr_year, usr_month):
    """ If current year is leap then add 1 day of feb if search day is beyond that """
    if (usr_year // 4 == 0) and (usr_month > 2):
        return 1
    else:
        return 0


# find day of specified date
def find_day_of_calendar(tareek):
    """ Find day of given date """
    # Find odd days 
    din_tareek, mahina, saal = tareek.day, tareek.month, tareek.year
    kul_din = 0

    # First find full year
    full_year = find_fullyear(saal)

    # Find leap years in full year from the start of the century
    kul_din = find_leapyears_in_fullyear(full_year)
    
    # Add odd days in a century as 1600 brabr = 0, 300 brabr = 1
    kul_din += odd_days_in_century_years(full_year)
    
    # Divide full year by 7 and add odd days
    kul_din += odd_days_in_full_year(full_year)
    
    # Add +1 for Feb as it has 29 days for the date after Feb in leap year
    kul_din += is_current_leapyear(usr_year=saal, usr_month=mahina)
    
    # Sum of odd days starting from January to one month less than user month
    # Slicing as it starts from 0
    kul_din += sum(odd_days_in_month[:mahina-1])
    
    # Add number of days of given month
    kul_din += din_tareek

    # Divide total odd days by 7 and remainder will show the specified day
    return kul_din % 7


tareek = date.today()
vaar = find_day_of_calendar(tareek)
print(f"{tareek.strftime("%d/%b/%Y")} : {vaar_names[vaar].title()}")
