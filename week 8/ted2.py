#Author:Rinat.R
#Date:11.15.25
#Problem 2:
"""checks if sum is > < or 10"""

def sum_check():
    x = float(input('enter first number:'))
    y = float(input('enter second number:'))

    total = x + y
    if total == 10:
        print('the sum is greater than 10')
    elif total < 10:
        print('the sum is less than 10')
    else:
        print('the sum is equal to 10')

sum_check()