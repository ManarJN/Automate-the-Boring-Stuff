#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 8 - Reading and Writing Files
# Multiclipboard - Saves and loads pieces of text to the clipboard.
    # Usage: ./8.2_multiclipboard.py save <keyword>   - saves clipboard to keyword
    #        ./8.2_multiclipboard.py <keyword>        - loads keyword to clipboard
    #        ./8.2_multiclipboard.py list             - loads all keywords to clipboard
    #        ./8.2_multiclipboard.py delete <keyword> - deletes keyword from shelf


import shelve, pyperclip, sys   #sys allows program to read terminal commands

mcbShelf = shelve.open('./8.2_files/8.2_shelf_clipboard/mcb')   # new piece of clipboard text will be saved to a shelf file

# saves clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':   # saves key and copied text to clipboard
    mcbShelf[sys.argv[2]] = pyperclip.paste()   
    print(sys.argv[2] + ': "' + pyperclip.paste() + '"' + ' saved to clipboard.')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] == 'all':
        mcbShelf.clear()
        print('Clipboard has been cleared.') 
    else:
        print(sys.argv[2] + ': "' +  mcbShelf[sys.argv[2]] + '"' + 'deleted from clipboard.')
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # lists keywords and loads content
    if sys.argv[1].lower() == 'list':   # prints list of shelf keys
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('The list of keys saved to your clipboard has been copied.')   
    elif sys.argv[1] in mcbShelf:   # loads key's value to clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])   
        print(sys.argv[1] + '\'s value has been copied.')

mcbShelf.close()
