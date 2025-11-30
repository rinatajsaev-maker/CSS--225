#Author:Rinat.R
#Date:11.02.25
#Problem 3:
"""print a random day of the week"""

import random
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_selected = random.choice(days)
print('random day of the week:', day_selected)