# -*- coding: utf-8 -*-

# ex16: Reading and Writing Files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Open the file in 'write' mode
target = open(filename, 'w')

# The truncate() is not necessary while opening the file with 'w' parameter.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

print "Now print the contents of the file."
target = open(filename)
print target.read()
