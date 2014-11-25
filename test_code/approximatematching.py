#!/usr/bin/python

# 
# Solve Minimum Skew problem: Find a position in a genome minimizing the skew
# Datafile: test10.data
#

import sys
import string
import fileinput
import re
import difflib
#import matplotlib.pyplot as plt

inputdata = []
pos       = []
posID     = [] 

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

pattern = inputdata[0]
dnastr  = inputdata[1]
mismatch= int(inputdata[2])
#print pattern, '\n', dnastr, '\n', mismatch, '\n'

for idx in range(0, len(dnastr)-len(pattern)+1):
#    obj = difflib.SequenceMatcher(None, pattern, dnastr[idx:idx+len(pattern)])
#    if obj.ratio() >= 0.625:
#        pos.append(idx)
    
    posID = [idy for idy in range(0, len(pattern)) if pattern[idy] == dnastr[idx+idy]]
#    print idx, len(posID)
    if len(posID) >= len(pattern) - mismatch:
        pos.append(idx)

print pos


