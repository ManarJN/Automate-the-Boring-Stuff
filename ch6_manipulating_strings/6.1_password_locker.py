#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 6- Manipulating Strings
# Password Locker - A program that insecurely stores passwords.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '1234'}

import sys, pyperclip

# returns message if program is called upon without an arg
# e.g. './6.1_password_locker.py'
# sys.argv is the line entered in the terminal to run the program
if len(sys.argv) < 2:   # 2 refers to './6.1_password_locker.py(1) arg(2)', items separated by space
    print('Usage: python 6.1_password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name
                        # [1] refers to e.g. './6.1_password_locker.py[0] blog[1]'


# if available, the password is copied to clipboard, otherwise it prints a message
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)



# to run program from terminal, type './6.1_password_locker.py args'
# e.g. './6.1_password_locker.py email' returns 'F7minlBDDuvMJuxESSKHFhTxFtjVB6'
