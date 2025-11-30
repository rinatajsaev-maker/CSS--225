#Author:Rinat.R
#Date:11.15.25
#Problem 4:
"""returns true if a year is leap year"""

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
year = int(input('enter a year: '))
print('leap year',is_leap(year))
