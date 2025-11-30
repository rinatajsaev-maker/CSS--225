#Name:Rinat.R
#Date:10.12.25
#Problem 7:
"""This program calculates the return day of the week after a given number of days"""
start = int(input("Enter start day number (0=Sun 6=Sat): "))
days = int(input("How many days you will be away? "))
back = (start + days) % 7
print("You will come back on day number", back)