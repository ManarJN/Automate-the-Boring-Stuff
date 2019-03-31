#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 11 - Web Scraping
# MapIt - Launches a map in the browser using an address from the command clipboard.

import pyperclip
import sys
import webbrowser

if len(sys.argv) > 1:
    # gets address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)