#!/usr/bin/python

import sys
import numpy as np
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y = 0
oldKey = None
thisKey = None
matrixTotal = np.matrix(0)
matrixTotal2 = np.matrix([0, 0, 0, 0])

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# outputs sum of matrix

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # print data_mapped
    if len(data_mapped) == 2:
        thisKey, y = data_mapped
        thisMatrix = np.matrix(y)
        if oldKey and oldKey != thisKey:
            print oldKey, "\t", matrixTotal
            oldKey = thisKey;
            matrixTotal = np.matrix([0])
        oldKey = thisKey
        matrixTotal = matrixTotal + thisMatrix


    #     CALCULATE xt x
    elif len(data_mapped) == 5:
        thisKey, x1, x2, x3, x4  = data_mapped
        thisMatrix2 = np.matrix([float(x1), float(x2), float(x3), float(x4)])
        # print thisMatrix
        if oldKey and oldKey != thisKey:
            print oldKey, "\t", matrixTotal
            oldKey = thisKey;
            matrixTotal = np.matrix([0, 0, 0, 0])
        oldKey = thisKey
        matrixTotal = matrixTotal + thisMatrix2

if oldKey != None:
    print oldKey, "\t", matrixTotal
