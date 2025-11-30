#Author:Rinat.R
#Date:11.23.25
#Problem 3:
"""Ask for numbers until their sum is over 100"""
numbers = []
total = 0

while total <= 100:
    value = float(input("Enter a number: "))
    numbers.append(value)
    total += value

print(numbers)
print(total)
