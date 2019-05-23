#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 15 - Keeping Time, Scheduling Tasks, and Launching Programs
# countdown - A simple countdown script

import subprocess
import time

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# at the end of the countdown, play a sound file
subprocess.Popen(['start', 'alarm.wav'], shell=True)
