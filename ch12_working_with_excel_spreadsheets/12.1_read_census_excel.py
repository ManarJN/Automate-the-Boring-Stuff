#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 12 - Working with Excel Worksheets
# Read Census Excel - Tabulates population and number of census tracts for each county.

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('./12.1_files/input_census_data/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # makes sure the key for this state exists
    countyData.setdefault(state, {})
    # makes sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # each row represents one census tract, so increments by one
    countyData[state][county]['tracts'] += 1
    # increases the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

# opens a new text file and writes the contents of countyData to it
print('Writing results...')
resultFile = open('./12.1_files/output_census_data/census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

# to see results of any county's data, just run import census2010 in interactive shell
# e.g.
# >>> import os
# >>> os.chdir('./12.1_files/output_census_data/census2010.py')
# >>> census2010.allData['AK']['Anchorage']
# >>> anchoragePop = census2010.allData['AK']['Anchorage']['pop']
# >>> print('The 2010 population of Anchorage was ' + str(anchoragePop))

# The 2010 opoulation of anchorage was 291826