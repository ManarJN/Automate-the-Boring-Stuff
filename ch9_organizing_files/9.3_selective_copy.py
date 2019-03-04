#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Selective Copy - Searches for files with a certain extension and copies them
#                  to a new folder


import os, shutil

def copy(source, destination, ext):
    # walks through folder
    for folderName, subfolders, filenames in os.walk(source):
        for filename in filenames:
            # move files that end with ext provided to destination
            if filename.endswith(ext):
                print('Copying %s from %s to %s.' % (filename, folderName, destination))
                shutil.copy(os.path.join(folderName, filename), destination)
                print('Done')

copy('./9.3_files/input_files', './9.3_files/output_files', '.txt')
