#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Rename Dates - Renames filenames with American MM-DD-YY date format
#                to European DD-MM_YYYY.


import shutil, os, re

# create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)  # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two digits for the day
    ((19|20)\d\d)                    # four digits for the year
    (.*?)$                           # all text after the date
    """, re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('./9.1_files/input_amerdates'):
    mo = datePattern.search(amerFilename)

    # skip files without a date
    if mo == None:
        continue
    print(amerFilename)
    # get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get the full, absolute file paths
    absWorkingDir = os.path.abspath('./9.1_files/input_amerdates')
    absWorkingDir2 = os.path.abspath('./9.1_files/output_eurodates')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir2, euroFilename)

    # rename the files and move to output folder
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  
