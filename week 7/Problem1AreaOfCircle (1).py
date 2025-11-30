#Author:Rinat.R
#Date:11.08.25
#Problem 1:
"""this program calculates the area of a circle """

import math
def areaOfCircle(r):
    area = math.pi * r ** 2
    return area

r = float(input("Enter radius:"))

print("the area of circle is", areaOfCircle(r))