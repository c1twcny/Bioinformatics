#!/usr/bin/python

#
# Datafile: test.data
#

import sys
import string
import fileinput
#import re

inputdata = []
genetic = {}
clump   = {}
maxfreq = 0
#maxfreqlist = []

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

tmpStr1 = inputdata[1].split()
inputdata.pop(len(inputdata)-1)
inputdata += tmpStr1
sequence  = inputdata[0]
kmers     = int(inputdata[1])
window    = int(inputdata[2])
frequency = int(inputdata[3])
maxlength = len(sequence)

#print kmers, window, frequency, maxlength

for idx in range(0, maxlength - window):
    for idy in range(idx, idx + window - kmers):
        if sequence[idy:idy + kmers] in genetic:
            genetic[sequence[idy:idy + kmers]] += 1
        else:
            genetic[sequence[idy:idy + kmers]] = 1
    for idz in range(0, len(genetic)):
        if genetic.items()[idz][1] == frequency:
#            print genetic.items()[idz][0]
            if genetic.items()[idz][0] in clump:
                clump[genetic.items()[idz][0]] += 1
            else:
                clump[genetic.items()[idz][0]]  = 1
    genetic = {}    # clean up dictionary before moving to the next window

print clump.keys()

