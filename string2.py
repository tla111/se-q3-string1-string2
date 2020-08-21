#!/usr/bin/env python3
"""
Kenzie assignment: String2
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Timothy La (tla111)"
"""
Referenced StackOverflow for the third problem
& Coach John W helped me with Problem 3
"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each of these string exercises in the same way as the
# previous String1 exercises.

# D. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    if len(s) >= 3 and s[-3:] == "ing":  # also could use endswith()
        return s + "ly"
    if len(s) >= 3:
        return s + "ing"
    else:
        return s

# Option 1 - If the length of s is greater than or equal to 3 and
#   the last three letters ends with "ing"
#       Output s with "ly" attached to the end of the string
# Option 2 - If the length of s is greater than or equal to 3
#   Output s with "ing" attached to the end of the string
# Option 3 - If the length of s is less than 3
#   Output s

# E. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'


def not_bad(s):
    notPos = s.find("not")
    badPos = s.find("bad")
    # if notPos < badPos and s.endswith("!"):
    if notPos < badPos and s.endswith("!"):
        return s[0:notPos] + "good" + "!"
    if notPos < badPos:
        return s[0:notPos] + "good"
    else:
        return s

# 1. Check to see whether s has the word "not" and store in a variable
# 2. Check to see whether s has the word "bad" and store in a variable
# Option 1 - If the word "not" is before "bad" in the string and
#   s ends with "!"
#       Output the words before "not" + "good" + "!"
# Option 2 - If the word "not" is before "bad" in the string
#   Output the words before "not" + "good"
# Option 3 - If the word "bad" is before "not"
#   Output s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the front
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back

# Used StackOverflow to help me
# https://stackoverflow.com
# /questions/31358564/finding-the-length-of-
# first-half-of-a-string-using-string-slicing-in-python


def front_back(a, b):
    frontCharA = ""
    frontCharB = ""
    backCharA = ""
    backCharB = ""
    if not len(a) % 2 == 0:
        frontCharA = a[0:len(a) // 2 + 1]
        backCharA = a[len(a) // 2 + 1:]
    if not len(b) % 2 == 0:
        frontCharB = b[0: len(b) // 2 + 1]
        backCharB = b[len(b) // 2 + 1:]
    if len(a) % 2 == 0:
        frontCharA = a[0:len(a) // 2]
        backCharA = a[len(a) // 2:]
    if len(b) % 2 == 0:
        frontCharB = b[0: len(b) // 2]
        backCharB = b[len(b) // 2:]
    return frontCharA + frontCharB + backCharA + backCharB

    # Option 1 - If the length of a is not divisible by 2
    #   Store the first half of the word plus the leftover letter
    #   Store the the second half of the word plus the leftover letter
    # Option 2 - If the length of b is not divisible by 2
    #   Store the first half of the word plus the leftover letter
    #   Store the the second half of the word plus the leftover letter
    # Option 3 - If the length of a is divisible by 2
    #   Store the first half of the word
    #   Store the the second half of the word
    # Option 4 - If the length of b is divisible by 2
    #   Store the first half of the word
    #   Store the the second half of the word
    # Output frontCharA + frontCharB + backCharA + backCharB

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swimming'), 'swimmingly')
    test(verbing('do'), 'do')

    print('\nnot_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print('\nfront_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
