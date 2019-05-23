#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 15 - Keeping Time, Scheduling Tasks, and Launching Programs
# Stopwatch - A simple stopwatch program

import time

# displays the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-C to quit')
input()  # press ENTER to begin
print('Started.')
starTime = time.time()  # gets the first lap's start time
lastTime = startTime
lapNum = 1

# starts tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  #resets the last lap time
except KeyboardInterrupt:
    # handles the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')