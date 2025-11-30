#Author:Rinat.R
#Date:11.02.25
#Problem 6:
"""this program calculates the factorial of a number"""
import math

num = int(input('enter a number:'))

factorial_manual = 1
for i in range(1, num + 1):
    factorial_manual *= 1
    factorial_math = math.factorial(num)

    print(factorial_manual)
    print(factorial_math)
