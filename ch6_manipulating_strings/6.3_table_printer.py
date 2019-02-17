#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 6- Manipulating Strings
# Table Printer - Program that displays a given list of strings in a neat table.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    # initializes a list with same number of values as number of groups in data 
    colWidths = [0] * len(data)

    # adds the length of each group's longest item to colWidths 
    for group in range(len(data)):   
        for item in data[group]:
            if len(item) > colWidths[group]:
                colWidths[group] = len(item)

    # assumes each group has the same number of items
    # prints the x value from each group, right justified with the length in colWidths
    for y in range(len(data[0])):   
        for x in range(len(data)):
            print(data[x][y].rjust(colWidths[x] + 1), end='')
        print('')

        
printTable(tableData)

