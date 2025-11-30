#Author:Rinat.R
#Date:11.08.25
#Problem 4:
"""this program returns a list of the unique numbers"""
def uniqueList(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique


my_list = [1, 3, 3, 3, 6, 2, 3, 5]
print("The unique elements of the list are:", uniqueList(my_list))