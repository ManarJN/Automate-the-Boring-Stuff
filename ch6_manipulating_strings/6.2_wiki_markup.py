#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 6- Manipulating Strings
# Wiki Markup - Adds Wikipedia bullet points to the start of each
#               line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

pyperclip.copy(text)