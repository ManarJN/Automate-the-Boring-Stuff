#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 11 - Web Scraping
# XKCD Download - Downloads every single XKCD comic.

import bs4
import os
import requests

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # stores comics in .xkcd
while not url.endswith('#'):
    # downloads the page
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # finds the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicURL = 'http:' + comicElem[0].get('src')
            # downloads the image
            print('Downloading image %s...' % (comicURL))
            res = requests.get(comicURL)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skips the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue

        # saves image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

