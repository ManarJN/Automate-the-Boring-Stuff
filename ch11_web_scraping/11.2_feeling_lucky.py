#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 11 - Web Scraping
# I'm Feeling Lucky - Opens several Google search results.

import bs4
import requests
import sys
import webbrowser

print('Googling...')  # display text while download the Google page
res = requests.get('http://google.com/search?q=' + ' '. join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
