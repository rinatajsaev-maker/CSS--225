#Name:Rinat.R
#Date:10.12.25
""" This program greets only specific users (you and your instructor)"""
#Problem 3:
name = input("Enter your name: ")
if name == "student" or name == "professor":
    print("Hello " + name + "!")
else:
    print("You are not allowed, sorry.")
