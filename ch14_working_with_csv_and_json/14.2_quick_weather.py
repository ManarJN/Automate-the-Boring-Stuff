#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 14 - Working with CSV and JSON
# Quick Weather - Prints the weather for a location from the command line

import json
import requests
import sys

# computes location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# downloads the JSON data from openweathermap.org's API
url = 'http://api.openweathermap.org/ata/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)  # returns a response object
response.raise_for_status()  # checks for errors in the response object
# downloaded text will be in response.text

# loads JSON data into a python variable
weatherData = json.loads(response.text)

# prints weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])



# downloaded JSON info looks like this, e.g.:
#{'city': {'coord': {'lat': 37.7771, 'lon': -122.42},
#          'country': 'United States of America',
#          'id': '5391959',
#          'name': 'San Francisco',
#          'population': 0},
#'cnt': 3,
#'cod': '200',
#'list': [{'clouds': 0,
#          'deg': 233,
#          'dt': 1402344000,
#          'humidity': 58,
#          'pressure': 1012.23,
#          'speed': 1.96,
#          'temp': {'day': 302.29,
#                   'eve': 296.46,
#                   'max': 302.29,
#                   'min': 289.77,
#                   'morn': 294.59,
#                   'night': 289.77},
#          'weather': [{'description': 'sky is clear',
#                       'icon': '01d',

# output would look like this, e.g.:
# entry: San Francisco, CA
# result:
#Current weather in San Francisco, CA:
#Clear - sky is clear

#Tomorrow:
#Clouds - few clouds

#Day after tomorrow:
#Clear - sky is clear