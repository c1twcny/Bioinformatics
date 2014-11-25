#!/usr/bin/python

import sys
import fileinput
import string
import operator
import time
import difflib
from collections import * 

inputdata = []    # original DNA string; might contain 'T'
inputdata1 = []   # transcribed RNA string by replacing 'T' with 'U' 
rna_codon_list = []
rna_codon = {}
tmplist = []
tmpkey = []
tmpvalue = []
rna = ''
dna = ''
pattern = [] 
newpattern = []
newmatch = []
k_mers = 3
tmpstr = []
peptide = []
peptidestr = ''
tmp1 = []
tmp2 = []
tmplist3 = ['']
tmplist4 = [] 
tmp5 = ''
tmplist6 = []
tmpdict = {}
npattern = 1
totalmatch = 0
teststr = ''
testlist = []
xlength  = 0
dnalength = 0
deltalength = 0
xincrement = 0
match      = False
skip       = False
newdnalist = []
reversecomplementmatch = []


start_time = time.time()

try:
    for line in fileinput.input():
        inputdata.append(line.rstrip())
except IOError:
    print "There is an error reading file."
    sys.exit()

#### Prepare input data
pattern = list(inputdata[-1])
dna = inputdata[-2]
rna = dna.replace('T','U') 
inputdata = inputdata[:-2] # list slicing to exclude the last two elements 
dnalength = len(dna)

###################################
# Function declaration block 
#
###################################
def reverseComplement(dna_string):
    l_dna = []
    l_dna_reverse = []
    l_dna_reverse_complement = []
    l_dna_reverse_complement_str = ''

    l_dna = dna_string
    l_dna_reverse = l_dna[::-1]

    for idx in range(len(l_dna_reverse)):
        if l_dna_reverse[idx] == ('A' or 'a'):
            element1 = 'T'
            l_dna_reverse_complement.append(element1.rstrip())
        elif l_dna_reverse[idx] == ('T' or 't'):
            element1 = 'A'
            l_dna_reverse_complement.append(element1.rstrip())
        elif l_dna_reverse[idx] == ('C' or 'c'):
            element1 = 'G'
            l_dna_reverse_complement.append(element1.rstrip())
        else:
            element1 = 'C'
            l_dna_reverse_complement.append(element1.rstrip())

    l_dna_reverse_complement_str = l_dna_reverse_complement_str. \
                                   join(l_dna_reverse_complement)

    return l_dna_reverse_complement_str


def reverseString(input_string):
    l_input_str = []
    l_reverse_str = []

    l_input_str = input_string
    l_reverse_str = l_input_str[::-1]

    return l_reverse_str


def complementString(input_string):
    l_dna_str = []
    l_complement = []
    l_complement_str = ''

    l_dna_str = input_string
    for idx in range(len(l_dna_str)):
        if l_dna_str[idx] == ('A' or 'a'):
            element1 = 'T'
            l_complement.append(element1.rstrip())
        elif l_dna_str[idx] == ('T' or 't'):
            element1 = 'A'
            l_complement.append(element1.rstrip())
        elif l_dna_str[idx] == ('C' or 'c'):
            element1 = 'G'
            l_complement.append(element1.rstrip())
        else:
            element1 = 'C'
            l_complement.append(element1.rstrip())

    l_complement_str = l_complement_str.join(l_complement)

    return l_complement_str


def findKmersMatch(dna_str, k_mers, pattern):
    l_dna       = dna_str 
    l_pattern   = pattern 
    l_k_mers    = k_mers
    l_match     = 0
    l_new_match = []
    l_length    = len(l_pattern[0])
    l_increment = 0
    l_skip      = False
    l_delta_length = len(dna_str) - l_length

    for x in l_pattern:
        l_match = 0
        for idx in range(l_delta_length):
            l_match = map(operator.eq, x, l_dna[idx:idx+len(x)]).count(True)
            if l_match == len(x):
                l_new_match.append(x)
                break

    return list(set(l_new_match))

def dnaKmersArray(dna_str, k_mers):
    l_dna        = dna_str
    l_k_mers     = k_mers
    l_dna_length = len(l_dna)

    dna_kmers_array = []

    for idx in range(l_dna_length - l_k_mers):
        dna_kmers_array.append(l_dna[idx:idx+l_k_mers])

    return dna_kmers_array 
#### Convert RNA codon/amino acid mapping table into python dictionary
tmplist = [[x for x in inputdata[idx].split()] for idx in range(len(inputdata))]
for idx in range(len(inputdata)):
    tmpkey.append(tmplist[idx][0])
    tmpvalue.append(tmplist[idx][1])

rna_codon = dict(zip(tmpkey, tmpvalue))

print 'Convert RNA codon/amino acid', time.time() - start_time, 'seconds'
 
#### Convert input DNA string into 3-mer RNA codon list 
for idx in range(0, len(rna)-k_mers+1, k_mers):
    tmpstr.append(rna[idx:idx+k_mers])

#### Map each RNA codon to corresponding amino acid
for idx in range(len(tmpstr)):
    if rna_codon[tmpstr[idx]] != 'X':
        peptide.append(rna_codon[tmpstr[idx]])

#### Join amino acids list into peptide
peptidestr = ''.join(peptide)

print 'Join amino acids list into peptide', time.time() - start_time, 'seconds'

#for idx in range(len(pattern)):
#    for key, value in rna_codon.iteritems():
#        if value == pattern[idx]:
#            print key
#print list(rna_codon.keys()) , len(list(rna_codon.keys()))
#print list(rna_codon.values()),len(list(rna_codon.values()))

#### Convert original <key:value> to <value:key> mapping
tmp = defaultdict(list)
for k, v in zip(rna_codon.values(), rna_codon.keys()):
    tmp[k].append(v)

for idx in range(len(tmp)):
    tmp1.append(tmp.items()[idx][0])  # Create a Key list
    tmp2.append(tmp.items()[idx][1])  # Create a Value list

tmpdict = dict([(k, v) for k,v in zip(tmp1, tmp2)])  # Create a tmp dictionary

print 'Convert to <value:key> mapping',time.time() - start_time, 'seconds'
#### Find all the possible DNA patterns
for x in pattern:
    tmplist4 = tmpdict.get(x)
    npattern *= len(tmplist4) 
    for idy in range(len(tmplist3)):
        tmp5 = tmplist3[idy]
#        print 'outer loop', idy, tmp5
        for idx in range(len(tmplist4)):
            tmplist3[idy] += tmplist4[idx]
            tmplist6.append(tmplist3[idy])
#            print 'inner looper', idx, tmplist6
            tmplist3[idy] = tmp5  # for inner loop only
    tmplist3 = tmplist6

for idx in range(len(tmplist6)):
    tmplist6[idx] = tmplist6[idx].replace('U', 'T')

newpattern = tmplist6[-npattern:]

print 'New DNA pattern list created', time.time() - start_time, 'seconds','\n'
#print 'Total number of patters', npattern, '\n'


xlength = len(newpattern[0])
deltalength = dnalength - xlength

print 'DNA kmers array length', len(dnaKmersArray(dna, xlength))
newdnalist = dnaKmersArray(dna, xlength)

for x in newpattern:
    testlist.append(reverseComplement(x))
    for y in newdnalist:
        if x == y:
            newmatch.append(x)
            break

#    for idx in range(deltalength):
#        match = map(operator.eq, x, dna[idx:idx+xlength]).count(True)
#        if match == len(x):
#            newmatch.append(x)
#            break



print 'Find exact forward matching pattern', time.time()-start_time,'seconds','\n'

for x in testlist:
    for y in newdnalist:
        if x == y:
            reversecomplementmatch.append(x)
            break

#reversecomplementmatch = findKmersMatch(dna, 0, testlist)

print newmatch + reversecomplementmatch
#print reversecomplementmatch
print 'Total number of patterns', npattern, 'Total execution time', \
       time.time() - start_time, "seconds"


