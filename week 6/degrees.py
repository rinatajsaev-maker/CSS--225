#Author:Rinat.R
#Date:11.02.25
#Problem 5:
"""this program converts radians to degrees"""

import math

radians =float(input('enter radians:'))
degrees_manual = radians * 180 / 3.14

degrees_math = math.degrees(radians)
print(degrees_math)
print(degrees_manual)
