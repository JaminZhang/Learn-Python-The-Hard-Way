# -*- coding: utf-8 -*-

# ex11: Asking Questions

# input(): Read a value from standard input. Equivalent to eval(raw_input(prompt)).
# raw_input(): Read a string from standard input. The trailing newline is stripped.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "Enter a integer: ",
num = int(raw_input())
print "The number you've input is: %d" % num

print "Enter a name: ",
name = raw_input()
print "What's %s's age?" % name,
age = input()
print "What's %s's height(in centimeters, input a integer)?" % name,
height = input()
print "What's %s's weight(in kilograms, input a integer)?" % name,
weight = input()
print "What's the color of %s's eyes?" % name,
eyes = raw_input()
print "What's the color of %s's teeth?" % name,
teeth = raw_input()
print "What's the color of %s's hair?" % name,
hair = raw_input()

type(name) # the data type of name will be <type 'str'>
type(age)  # the data type of age will be <type 'int'>

print "Let's talk about %s." % name
print "He's %d years old." % age
print "He's %d centimeters tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print 'If I add %d, %d and %d I get %d.' % (age, height, weight, age + height + weight)

s = raw_input('---> ')
print s

s = raw_input('What is your favorite food? ')
print "Favorite food: %r" % s
