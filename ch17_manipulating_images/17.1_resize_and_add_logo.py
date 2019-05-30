#! /usr/bin/env python3

# Automate the Boring Stuff
# Chapter 17 - Manipulating Images
# Resize and Add Logo - Resizes all images in current working directory to fit in
#                       a 300x300 square and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = './17.1_files/17.1_input_photos/catlogo.png'
PIC_FOLDER = './17.1_files/17.1_input_photos'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('./17.1_files/17.1_output_photos', exist_ok=True)

# loops over all files in the working directory
for filename in os.listdir('./17.1_files/17.1_input_photos'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == os.path.basename(LOGO_FILENAME):
        continue  # skips non-image files and the logo file itself

    im = Image.open(os.path.join(PIC_FOLDER, filename))
    width, height = im.size

    # checks if the image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # calculates the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    # resizes the image
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))

    # adds the logo
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height-logoHeight), logoIm)
      # if 3rd argument in .paste() is omited, transparent pixels in logo will be
      # copied as solid white pixels

    # saves changes
    im.save(os.path.join('./17.1_files/17.1_output_photos', filename))