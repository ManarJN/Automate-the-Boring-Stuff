#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 8 - Reading and Writing Files
# Regex Search - Opens all .txt files in a folder and searches for any line that
#                matches a user-supplied regular expression.


import re, os

# asks user for search expression and location
userSearch = input('What would you like to search for?\n')
regex = re.compile(userSearch, re.I)   

while True:
    folder = input('Please enter the absolute path of the folder you want to search: ')
    if os.path.exists(folder) == False:
        print('This folder does not exist.')
        continue
    else:
        folderList = os.listdir(folder)
        break

    
# opens all .txt files in a folder and searches for expression
textLocations = []  # initalizes list of documents that contain expression
for file in folderList:
    filePath = os.path.join(folder, file)
    if filePath.endswith('.txt'):  # finds .txt files
        searchFile = open(filePath)
        searchText = searchFile.read()
        foundText = regex.findall(searchText)
        searchFile.close()
        if foundText != []:  # adds documents that contain expression to list
            textLocations += [file]

# if expression is not found in folder            
if textLocations is None:
    print(userSearch + ' was not found in the folder specified.')

# if expression is found in folder
elif textLocations is not None:
    print(userSearch + ' was found in the following documents: ')
    for location in textLocations:
        print(location)
        







  
