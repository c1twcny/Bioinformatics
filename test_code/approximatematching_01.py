#!/usr/bin/python

# 
# Solve Minimum Skew problem: Find a position in a genome minimizing the skew
# Datafile: test10.data
#

import sys
import string
import fileinput
import operator

inputdata = []
pos       = []
totalmatch = 0 

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

pattern = inputdata[0]
dnastr  = inputdata[1]
mismatch= int(inputdata[2])
#print pattern, '\n', dnastr, '\n', mismatch, '\n'

for idx in range(0, len(dnastr)-len(pattern)+1):
    totalmatch = map(operator.eq, pattern, dnastr[idx:idx+len(pattern)]).count(True)    # First method
#    totalmatch = [x == y for (x, y) in zip(pattern, dnastr[idx:idx+len(pattern)])].count(True) # Second method  
    if totalmatch >= len(pattern) - mismatch:
        pos.append(idx)

print pos


