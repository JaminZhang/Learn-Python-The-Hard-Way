# -*- coding: utf-8 -*-

# ex05: More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
    age, height, weight, age + height + weight)

# Try more format characters
my_greeting = "Hello,\t"
my_first_name = "Jamin"
my_last_name = "Zhang"
my_age = 27

# Print 'Hello,\t' my name is Jamin Zhang, and I'm 27 years old.
print "%rmy name is %s %s, and I'm %d years old." % (my_greeting, my_first_name, my_last_name, my_age)

# Try to write some variables that convert the inches and pounds to centimeters and kilograms.
centimeters_per_inch = 2.54
kilograms_per_pound = 0.4535923

print "He's %f centimeters tall." % (height * centimeters_per_inch)
print "He's %f kilograms heavy." % (weight * kilograms_per_pound)
