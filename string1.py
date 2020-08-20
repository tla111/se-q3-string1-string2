#!/usr/bin/env python3
"""
Kenzie assignment: String1
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Timothy La (tla111)"

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Example:
#   donuts(5) returns 'Number of donuts: 5'
#   donuts(23) returns 'Number of donuts: many'


def donuts(count):
    if count < 10:
        return "Number of donuts: " + str(count)
    else:
        return "Number of donuts: many"

# Option 1 - If the count is less than 10
    # The function will print "Number of donuts: " + the count
        # Need to turn the number into a string to concat with the string,
        # "Number of donuts: "
# Option 2 - If the count is greater than 10
    # The function will print out "Number of donuts: many"

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 characters of the original string.
# However, if the string length is less than 2, return
# an empty string instead.
# Example:
#   'spring' -> 'spng'


def both_ends(s):
    if len(s) > 2:
        return s[0:2] + s[-2:]
    else:
        return ""

# Option 1 - If s (the string) has more than 2 characters
    # Split the first two letters of the string [0:2]
    # Split the last two letters of the string
    # Combine the two
        # [Where to start : Where to end]
# Option 2 - If s (the string) has less than 2 characters
    # Output an empty string

# C. fix_start
# Given a string s, return a string where all occurrences
# of its first character have been changed to '*', except
# do not change the first character itself.
# Example:
#   'babble' -> 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    part_word = s.replace(s[0], "*")
    slice_word = part_word[1:]
    return s[0] + slice_word

# 1. Use the replace method to turn the letters of the string that matches
    # the first letter into the special character "*"
    # and store it into a variable to be used later
# 2. Slice the string from part_word and store all the letters
    # after the first letters into a variable
# 3. Combine the first letter of the string that has not been modified with
    # slice_word (the modified string with the "*" as letters)

# D. mix_up
# Given strings a and b, return a single string with a and
# b separated by a space '<a> <b>', except swap the first
# 2 characters of each string.
# Example:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    first_word = a[0:2] + b[2:]
    second_word = b[0:2] + a[2:]
    return second_word + " " + first_word

# 1. Store the first two letters of a and
    # the letters after the first two characters of b into a variable
# 2. Store the first two letters of b and
    # the letters after the first two charaters of a into a variable
# 3. Output the second variable + a space (" ") + the first variable


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}    expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('\nboth_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('\nfix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print('\nmix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
