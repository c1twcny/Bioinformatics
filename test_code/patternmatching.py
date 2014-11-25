#!/usr/bin/python

# 
# Pattern matching: find all occurrences of a pattern in a string
# Datafile: test06.data
#
import fileinput
import sys
import string
import re

inputdata = []
matchlist = []
matchposition = []
newmatchposition = []

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

inputdata = filter(None, inputdata)    # remove empty strings from a list
#print '[Pattern, Input-string]:', inputdata

str0 = inputdata[0]
str1 = inputdata[1]

pattern1 = re.compile(str0)
iterator = pattern1.finditer(str1)
for match in iterator:
    matchlist.append(match.span())

matchposition = [matchlist[idx][0] for idx in range(0, len(matchlist))]

#print matchposition

for idx in range(len(matchlist)):
    for idy in range(matchlist[idx][0],matchlist[idx][1]):
#        print str1[idy:idy+len(str0)]
        if str1[idy:idy+len(str0)] == str0:
            newmatchposition.append(idy)

print newmatchposition


