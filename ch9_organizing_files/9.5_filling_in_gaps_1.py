#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Filling in the Gaps 1 - Finds all files with a given prefix, locates gaps in the
#                         numbering, and renames files accordingly.

import os
import re
import shutil


def gap_finder(source, destination, prefix):
    regex = re.compile(prefix + r'(\d+).(.*?)$')
    files = os.listdir(source)  # creates a list of files in source
    
    # finds files with given prefix
    number_list = []
    for file in files:
        match = regex.search(file)
        if match is None:
            continue
        number_list += [int(match.group(1))]  # creates list of file numbers in integer form
    
    # checks if file numbering and number of files in folder don't match
    if (max(number_list) - min(number_list) + 1) > len(files):
        item = min(number_list)  # in case file numbering starts at a number other than 1
        for file in files:

            # run regex search again
            match = regex.search(file)
            if match is None:
                continue
            number = match.group(1)
            ext = match.group(2)

            # renames incorrectly numbered files
            if number != str(item).zfill(len(number)):
                new_name = prefix + str(item).zfill(len(number)) + '.' + ext
                shutil.copy(os.path.join(source, file), os.path.join(destination, new_name))
            item += 1
                

gap_finder('./9.5_files/input_incorrectly_numbered_files', './9.5_files/output_correctly_numbered_files', 'spam')
