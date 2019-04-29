#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 11 - Web Scraping
# Command Line Emailer - Sends email via command line.

import sys
import time
from selenium import webdriver

# returns message if program is called upon without an arg
if len(sys.argv) < 2:
    print('Usage: python 11.4_command_line_emailer.py emailaddress text')
    sys.exit()

# assigns arguments to variables
email = sys.argv[1]
text = "".join(sys.argv[2:])

browser = webdriver.Firefox()
browser.get('https://gmail.com')
email.send_keys('study.shortcut.summary@gmail.com')

signin = browser.find_element_by_class('h-c-header__nav-li-link')
signin.click()
time.sleep(5)

# htmlElem = browser.find_element_by_tag_name('html')
# html.send_keys(Keys.TAB)

# https://www.reddit.com/r/learnpython/comments/8b7ig9/practice_projects_in_the_chapter_11_of_automate/