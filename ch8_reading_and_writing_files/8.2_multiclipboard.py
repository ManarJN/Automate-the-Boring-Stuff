#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 8 - Reading and Writing Files
# Multiclipboard - Saves and loads pieces of text to the clipboard.
    # Usage: ./multiclipboard.py save <keyword> - saves clipboard to keyword
    #        ./multiclipboard.py <keyword>      - loads keyword to clipboard
    #        ./multiclipboard.py list           - loads all keywords to clipboard


import shelve, pyperclip, sys   #sys allows program to read terminal commands

mcbShelf = shelve.open('./8.2_shelves/mcb')   # new piece of clipboard text will be saved to a shelf file

# saves clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()   # saves key and text to clipboard
elif len(sys.argv) == 2:
    # lists keywords and loads content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))   # list of shelf keys is copied to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])   # loads key's value to clipboard

mcbShelf.close
