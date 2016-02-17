#!/usr/bin/python

'''
formula:
y = BX
y = B0 + B1 * x1 + B2 * x2 + B3 * x3

This script is the first step in creating matrix A, or computing coefficients in the linear regression:
B0, B1, B2, B3

Mappers calculate matrix A by emitting two types of tuples, combined for form a matrix:

Type 1: matrix A
(row1, x * transpose(x))
(row2, x * transpose(x))
.
.
.

Type 2: vector b
(row 1, x*y)
(row 2, x*y)
.
.
.


Reducers sum above matrices by row, producing two final matrices:
A = sum all Type 1 tuples from mapper
b = sum all Type 2 tuples from mapper

final solution to calculate coefficients is
B = inverse(A) * b
'''

# testfile | ./mapper.py

import sys
import pandas as pd
import numpy as np
import os

dirLoc = os.path.dirname(os.path.realpath(__file__))
data = pd.read_csv(dirLoc + "/trainNew.csv", sep = "\t" )
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




