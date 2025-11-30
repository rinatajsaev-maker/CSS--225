#Author:Rinat.R
#Date:11.08.25
#Problem 2:
"""this program checks if a number is in the range"""

def checkRange(num):
    if num in range(1, 10):
        print(num, "is in the range.")
    else:
        print(num, "is not in the range.")


checkRange(5)
checkRange(12)