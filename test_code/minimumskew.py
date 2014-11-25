#!/usr/bin/python

# 
# Solve Minimum Skew problem: Find a position in a genome minimizing the skew
# Datafile: test09.data
#

import sys
import string
import fileinput
import re
import matplotlib.pyplot as plt

inputdata = []
mlistG = []
mlistC = []
runningtotal = [0]
totalG = 0
totalC = 0

for line in fileinput.input():
    inputdata.append(line.rstrip());    # strip out newline character

#print inputdata, len(inputdata[0])

inputstr = inputdata[0]
p_g = re.compile('G')
p_c = re.compile('C')
iteratorG = p_g.finditer(inputstr)
iteratorC = p_c.finditer(inputstr)

for match in iteratorG:
    mlistG.append(match.span())

for match in iteratorC:
    mlistC.append(match.span())

#print [mlistG[idx][0] for idx in range(0, len(mlistG))], len(mlistG)
#print [mlistC[idx][0] for idx in range(0, len(mlistC))], len(mlistC)

for idx in range(0, len(inputstr)):
    if inputstr[idx] == 'G':
        totalG += 1
    elif inputstr[idx] == 'C':
        totalC += 1

    runningtotal.append(totalG-totalC)

minGC = min(runningtotal)
#print runningtotal
for idx in range(0, len(runningtotal)):
    if runningtotal[idx] == minGC: 
        print idx


plt.plot(runningtotal)
plt.show()

