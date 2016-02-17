#!/usr/bin/python
'''
given features, what is the probability of Y?
p(Y | x) = p(x | Y) p(Y) / P(x)
p(Y | x) = p(x | Y) p(Y) / [ p(x | Y) p(Y) + p(x | not-Y) p(not-Y)]
this mapper emits tuples that are used for predictions on a pre-specified feature set.
As an example, Y and X are initialized as first row from input dataset

to calculate final prediction, take the output from the reducer and apply:
p(Y | x) = tupple(x|Y) * tupple(Y) / tupple(X)
'''


import sys
import pandas as pd
import numpy as np
import os

dirLoc = os.path.dirname(os.path.realpath(__file__))
dfY = pd.read_csv(dirLoc + "/trainDependant.csv", sep = "\t")
dfX = pd.read_csv(dirLoc +  "/trainIndependant.csv", sep = "\t")

# initialize Y, X in example:
predInput = dfY.iloc[1,:]
print('Prob Y = ' + predInput)
featInput = dfX.iloc[1,:]
print('Given features = ' + featInput)

dfX.iloc[1,:] == dfX.iloc[1,:]

for i in range(1, dfY.shape[0]):
    # P(x)
    if all(featInput == dfX.iloc[i,:]):
        print("{0}\t{1}".format('x', 1))
    else:
        print("{0}\t{1}".format('x', 0))

    # p(Y)
    if all(predInput == dfY.iloc[i,:]):
        print("{0}\t{1}".format('y', 1))

        # p(x | Y)
        if all(featInput == dfX.iloc[i,:]):
            print("{0}\t{1}".format('x|y', 1))
        else:
            print("{0}\t{1}".format('x|y', 0))

    else:
        print("{0}\t{1}".format('y', 0))








