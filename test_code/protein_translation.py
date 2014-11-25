#!/usr/bin/python
# 
# Created: TWC
# Date:
# Version:
#
# Input: rna_codon.data test02.data
# Output: amino acid list
#

import sys
import fileinput
import string
import operator

rna_codon  = {}
inputdata  = []
tmpstr     = []
tmplist    = []
tmpkey     = []
tmpvalue   = []
peptide    = []
dna        = ''
rna        = ''
peptidestr = ''
k_mers     = 3

try:
    for line in fileinput.input():
        inputdata.append(line.rstrip())
except IOError:
    print "There is an error reading file."
    sys.exit()

dna = inputdata[-1]
rna = dna.replace('T', 'U') 
inputdata.pop(-1)

# Create a complete RNA codon dictionary name "rna_codon"
tmplist = [[x for x in inputdata[idx].split()] for idx in range(len(inputdata))]
for idx in range(len(inputdata)):
    tmpkey.append(tmplist[idx][0])
    tmpvalue.append(tmplist[idx][1])
rna_codon = dict(zip(tmpkey, tmpvalue))

# Segment input RNA string into list of codon 
for idx in range(0, len(rna)-k_mers+1, k_mers):
    tmpstr.append(rna[idx:idx+k_mers])

# Translate codon list into amino acid list using rna_codon mapping dictionary 
for idx in range(len(tmpstr)):
    if rna_codon[tmpstr[idx]] != 'X':
        peptide.append(rna_codon[tmpstr[idx]])

peptidestr = ''.join(peptide)
print peptidestr

