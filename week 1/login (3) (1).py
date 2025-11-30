#!/usr/bin/env python3
""" 
Author: Antonio
Date:09/28/25
Course- Css-225

this program asks the user for a username and password
and prints a message if login is successful
"""
username = input("Login: >> ")
user1 = "Jack"
user2 = "Jill"
if username == user1:
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
else:
    print("Access denied")
