#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 8 - Reading and Writing Files
# MadLibs - Reads a madlib file and lets user add text.

import re

# reads madlibs file
madlibFile = open('./8.3_files/8.3_input_madlibs/madlib.txt')
madlibText = madlibFile.read()
madlibFile.close


#regex
regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
madlibList = regex.findall(madlibText)  # creates a list of found search words


# searches for words and replaces them with user entry
for item in madlibList:
    #provides grammatically correct a/an
    if item == 'ADJECTIVE':
        replace = 'an adjective'
    elif item == 'NOUN':
        replace = 'a noun'
    elif item == 'ADVERB':
        replace = 'an adverb'
    elif item == 'VERB':
        replace = 'a verb'

    matchRegex = re.compile(item)    
    madlibText = matchRegex.sub(input('Please enter %s: ' % replace), madlibText, count=1)  # replaces madlib text with user entry


# ouputs new file with user text
madlibOutput = open('./8.3_files/8.3_output_madlibs/madlib_result', 'w')
madlibOutput.write(madlibText)
madlibOutput.close()
print('Madlib has been saved.')



  
