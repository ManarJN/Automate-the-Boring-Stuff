#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 13 - Working with PDF and Word
# Combine PDFs - Combines all the PDFs in the current working directory
#                into a single PDF.

import os
import PyPDF2

# gets all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# loops through all the PDF files
for filename in pdfFiles:
    # loops through all the pages (except the first) and adds them
    for pageNum in range(1, pdfReader.numPages):
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# saves the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()