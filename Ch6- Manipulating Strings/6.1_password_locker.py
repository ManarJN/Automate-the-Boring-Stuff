#! /usr/bin/env python3.

#automate the boring stuff
#chapter 3- manipulating strings
#password locker - a program that insecurely stores passwords

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '1234'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python 6.1_password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
