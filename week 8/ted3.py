#Author:Rinat.R
#Date:11.15.25
#Problem 3:
"""checks if the number 5 is in a given list"""

def find_five():
    nums = input('enter numbers separated by spaces')
    nums = [int(n) for n in nums.split()]

    if 5 in nums:
        print('5 is in the list')
    else:
        print('5 is not in the list')

find_five()

