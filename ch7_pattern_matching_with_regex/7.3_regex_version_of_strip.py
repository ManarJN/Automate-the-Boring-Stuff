# Automate the Boring Stuff
# Chapter 7- Pattern Matching with Regex
# Regex Version of strip() - Performs a strip() function using Regex.

import re

# defines strip function
def regexStrip(string, remove=''):
    if remove == '':   # if no characters are specified, strip whitespace characters
        stripLeft = re.compile(r'^\s*')
        stripRight = re.compile(r'\s*$')
        
        newString = stripLeft.sub('',string)
        newString = stripRight.sub('',newString)
    else:  # if characters are specified, strip the characters
        stripLeft = re.compile(r'^[' + remove + ']*')
        stripRight = re.compile(r'[' + remove + ']*$')
        
        newString = stripLeft.sub('',string)
        newString = stripRight.sub('',newString)
    print(newString)


# calls on strip function
string = input('Please enter a string to strip: ')
remove = input('Please enter the character(s) you want stripped.\nIf nothing is \
entered, whitespace characters will be stripped: ')
regexStrip(string, remove)

