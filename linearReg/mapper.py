#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

# testfile | ./mapper.py

import sys
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/dallammasterson/gitRepos/mapReduce/linearReg/trainNew.csv", sep = "\t" )
dataM = np.matrix(data)

# need to functionalize
for i in range(0, dataM.shape[0]):
    # output by row xt * x
    A = np.dot(dataM[i, 0:4].transpose(), dataM[i, 0:4])
    a1 = 'a1\t' + str(A[0, 0]) + '\t' +  str(A[0, 1]) + '\t' +  str(A[0, 2]) + '\t' +  str(A[0, 3])
    a2 = 'a2\t' + str(A[1, 0]) + '\t' +  str(A[1, 1]) + '\t' +  str(A[1, 2]) + '\t' +  str(A[1, 3])
    a3 = 'a3\t' + str(A[2, 0]) + '\t' +  str(A[2, 1]) + '\t' +  str(A[2, 2]) + '\t' +  str(A[2, 3])
    a4 = 'a4\t' + str(A[3, 0]) + '\t' +  str(A[3, 1]) + '\t' +  str(A[3, 2]) + '\t' +  str(A[3, 3])

    B = np.dot(dataM[i, 0:4].transpose(), dataM[i, 4])
    b1 = 'b1\t' + str(B[0, 0])
    b2 = 'b2\t' + str(B[1, 0])
    b3 = 'b3\t' + str(B[2, 0])
    b4 = 'b4\t' + str(B[3, 0])

    # print rows
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(b1)
    print(b2)
    print(b3)
    print(b4)




