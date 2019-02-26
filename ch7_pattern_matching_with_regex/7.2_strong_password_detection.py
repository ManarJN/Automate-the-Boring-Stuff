#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 7- Pattern Matching with Regex
# Strong Password Detection - Ensures a password is strong.

import re

# creates password regex
pwLowCase = re.compile(r'[a-z]')   # checks for a lowercase letter
pwUpCase = re.compile(r'[A-Z]')    # checks for an uppercase letter
pwNum = re.compile(r'\d')          # checks for a number
pwSpace = re.compile(r'\s')        # checks for spaces, tabs, or newline characters

# defines pw strength checker function on user input
def pwRegex(password):
    strong = True
    if len(password) < 8:
        print('Your password must be at least 8 characters long.')
        strong = False
    if pwLowCase.search(password) is None:
        print('Your password must contain a lowercase character.')
        strong = False
    if pwUpCase.search(password) is None:
        print('Your password must contain an uppercase character.')
        strong = False
    if pwSpace.search(password) is not None:
        print('Your password cannot contain spaces, tabs, or newline characters.')
        strong = False
    if strong:   # if password passes above criteria
        print('Your password is strong.')
        

# calls pw strength checker function
password = input('Please enter a password: ')
pwRegex(password)
