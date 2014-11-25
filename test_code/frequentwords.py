#!/usr/bin/python

#
# Finding k-mers in DNA sequence
#
# datafile: test03.data
#
# Need two inputs: (1) DNA sequence, and (2) k-mers
# 

import fileinput
import sys
import string

inputdata = []
inputdata1 = []
inputdata2 = []
genetic = {}
maxfreq = 0
maxfreqlist = []

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

#print inputdata
inputdata2 = inputdata[len(inputdata)-1]    # extract the last element
inputdata.pop(len(inputdata)-1)        # pop the last element in inputdata
inputdata1 = ''.join(inputdata)        # eliminate white space
#print inputdata2
#print inputdata1
inputdata = []                         # empty the inputdata list
inputdata = [inputdata1, inputdata2]   # populate inputdata with new elements
#inputdata1 = string.join(inputdata).replace(" ","")
#print string.join(inputdata).replace(" ","")
#print string.join(inputdata)

#print 'length of the elements:', len(inputdata1)

for idx in range(0, len(inputdata[0])):
    if idx+int(inputdata[1]) <= len(inputdata[0]):
#        print inputdata[0][idx:idx+int(inputdata[1])]
        if inputdata[0][idx:idx+int(inputdata[1])] in genetic:
            genetic[inputdata[0][idx:idx+int(inputdata[1])]] += 1
        else:
            genetic[inputdata[0][idx:idx+int(inputdata[1])]] = 1
#print genetic

maxfreq = max(genetic.values())
maxlen  = len(genetic)

for i in range(0,maxlen):
    if genetic.items()[i][1] == maxfreq:
        maxfreqlist.append(genetic.items()[i][0])

print '\n', 'The list of most frequent word(s):'
print maxfreqlist
#print [x[::-1] for x in maxfreqlist]    # reversed sequence
