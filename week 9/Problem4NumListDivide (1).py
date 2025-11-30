#Author:Rinat.R
#Date:11.23.25
#Problem 4:
"""Collect number from 0 to 50 divisible by 10"""
tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(tens)
