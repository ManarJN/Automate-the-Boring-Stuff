#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 16 - Sending Emails and Texts
# Text Myself - Defines the textmyself() function that texts a message passed
#               to it as a string

# preset values from TWILIO
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'
twilioNumber = '+15552225678'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)