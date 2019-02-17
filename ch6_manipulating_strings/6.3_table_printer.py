#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 6- Manipulating Strings
# Table Printer - Program that displays a given list of strings in a table.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data)   # empty list with same number of values as number of lists in data 
    for group in range(len(data)):   
        for item in data[group]:
            if len(item) > colWidths[group]:
                colWidths[group] = len(item)

    for y in range(len(data[0])):   # assumes every group has the same number of items
        for x in range(len(data)):
            print(data[x][y].rjust(colWidths[x]+1), end='')
        print('')
        
printTable(tableData)


