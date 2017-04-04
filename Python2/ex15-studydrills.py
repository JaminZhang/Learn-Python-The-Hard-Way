# -*- coding: utf-8 -*-

# ex15: Reading Files

# Import argv variable from sys submoudle
from sys import argv

# Unpack the argv variable
script, filename = argv

# Open a file
txt = open(filename)

# Print the filename, then print all the contents of the file
print "Here's your file %r:" % filename
#print txt.read()
#print txt.readline()
print txt.readlines()

# Close the file
txt.close()

# Prompt to type the filename again
print "Type the filename again:"
# Input the new filename
file_again = raw_input("> ")

# Open the new select file
txt_again = open(file_again)

# Print the contents of the new selected file
print txt_again.read()

# Close the file
txt_again.close()
