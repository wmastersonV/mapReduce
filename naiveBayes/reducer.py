#!/usr/bin/python

import sys
import pdb

counter = 1
numTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisNum = data_mapped
    thisNum = int(thisNum)

    if oldKey and oldKey != thisKey:
        print(oldKey, float(numTotal) / float(counter))
        oldKey = thisKey;
        numTotal = 0
        counter = 0

    oldKey = thisKey
    numTotal += thisNum
    counter += 1

if oldKey != None:
    print(oldKey, float(numTotal) / float(counter))

