#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 14 - Working with CSV and JSON
# Remove CSV Header - Removes the header from all CSV files in the current
#                     working directory

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# loops through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # skips non-csv files

print('Removing header from ' + csvFilename + '...')

# reads the csv file in (skipping first row)
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue  # skips first row
    csvRows.append(row)
csvFileObj.close()

# writes out the csv file
csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()

