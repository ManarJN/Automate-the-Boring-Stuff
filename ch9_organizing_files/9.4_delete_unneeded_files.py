#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Delete Unneeded Files - Walks through a folder and searches for large files
#                         and folders


import os

def bigFiles(source, size):
    # walks through folder
    for folderName, subfolders, filenames in (os.walk(source)):
        # finds large files
        for filename in filenames:
            if os.path.getsize(os.path.join(folderName, filename)) > size:
                print(os.path.abspath(filename) + ' is larger than ' + str(size) + 'B.')

bigFiles('./9.4_files/input_files', 15000)
