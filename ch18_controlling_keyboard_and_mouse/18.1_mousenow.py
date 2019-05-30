#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 18 - Controlling the Keyboard and Mouse with GUI Automation
# Mousenow - Displays the mouse cursor's current position

import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        # gets and prints the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')

