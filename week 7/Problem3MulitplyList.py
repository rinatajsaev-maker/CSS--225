#Author:Rinat.R
#Date:11.08.25
#Problem 3:
"""this program multiplies all numbers in a list"""

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [6, 3, 8, -1]
print("The multiplication of all numbers in the list is:", multiplyList(my_list))