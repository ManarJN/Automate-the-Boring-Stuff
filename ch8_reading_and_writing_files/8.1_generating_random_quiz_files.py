#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 8 - Reading and Writing Files
# Generating Random Quiz Files - Creates quizzes with questions and answers in
#                                random order, along with answer key.

import random

# the quiz data
# keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
            'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generates 10 quiz files
for quizNum in range(10):
    
    # creates quiz and answer key files
    quizFile = open('./8.1_files/8.1_output_quizzes/capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('./8.1_files/8.1_output_answers/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # writes out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffles the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # loops through all 50 states, making a question for each
    for questionNum in range(50):
        
        #gets right and wrong ansewrs
        correctAnswer = capitals[states[questionNum]]         # loops through the shuffled states list, finds each state in capitals, and stores the state's coresponding capital in correct answer
        wrongAnswers = list(capitals.values())                # duplicates all values in capitals dictionary
        del wrongAnswers[wrongAnswers.index(correctAnswer)]   # deletes the correct answer
        wrongAnswers = random.sample(wrongAnswers, 3)         # selects 3 random values from the list    
        answerOptions = wrongAnswers + [correctAnswer]        # combines 3 wrong answers and right answer into a list
        random.shuffle(answerOptions)                         # randomizes answers so correct response isn't always D

        # writes the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):   
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))   # 'ABCD'[i] treats 'ABCD' as an array and loops through each letters
        quizFile.write('\n')

        # writes the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))   # finds integer index of correct answer 

quizFile.close()
answerKeyFile.close()














        
