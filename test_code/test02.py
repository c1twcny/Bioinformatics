#!/usr/bin/python

# Find reverse complement of input nucleotide pattern
#
# datafile: test05.data
#

import sys
import fileinput
import string

inputdata = []
reversedata = []
revcomplement = []
revcomplementstr = ''

# read from a data file
for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

# reverse the sequence
reversedata = [x[::-1] for x in inputdata]

# change to complement
for idx in range(0,len(reversedata[0])):
    if reversedata[0][idx] == ('A' or 'a'):
        element1 = 'T'
        revcomplement.append(element1.rstrip())
    elif reversedata[0][idx] == ('T' or 't'):
        element1 = 'A'
        revcomplement.append(element1.rstrip())
    elif reversedata[0][idx] == ('C' or 'c'):
        element1 = 'G'
        revcomplement.append(element1.rstrip())
    else:
        element1 = 'C'
        revcomplement.append(element1.rstrip())
#    print reversedata[0][idx], revcomplement

revcomplementstr = revcomplementstr.join(revcomplement)
print  revcomplementstr


