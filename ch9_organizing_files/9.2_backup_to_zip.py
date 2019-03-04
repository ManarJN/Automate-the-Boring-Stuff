#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 9 - Organizing Files
# Backup to Zip - Copies an entire folder and its contents into a ZIP file
#                 whose filename increments.


import zipfile, os

def backupToZip(folder, zipLocation):
    # backup the entire contents of "folder" into a ZIP file

    # figure out the filename this code should be based on
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists('./9.2_files/output_zipfiles/' + zipFilename):
            break
        number += 1

    # create the ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile('./9.2_files/output_zipfiles/' + zipFilename, 'w')

    # walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        
        # add the current folder to the ZIP file
        backupZip.write(foldername)

        # add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('./9.2_files/input_folder/test_folder', './9.2_files/output_zipfiles')
