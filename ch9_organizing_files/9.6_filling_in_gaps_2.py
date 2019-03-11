#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Filling in the Gaps 2 - Inserts gaps into numbered files so new file can be added

import os
import re
import shutil


def gap_maker(source, destination, prefix, file_number):
    regex = re.compile(prefix + r'(\d+).(.*?)$')
    files = os.listdir(source)  # creates a list of files in source

    # finds files with given prefix
    for file in files:
        match = regex.search(file)
        if match is None:
            continue

        # find file with given file number
        number = match.group(1)
        ext = match.group(2)
        if int(number) >= int(file_number):
            new_number = int(number) + 1
            new_name = prefix + str(new_number).zfill(len(number)) + '.' + ext
            shutil.copy(os.path.join(source, file), os.path.join(destination, new_name))


gap_maker('./9.6_files/input_numbered_files', './9.6_files/output_numbered_files_and_gap', 'spam', '004')
