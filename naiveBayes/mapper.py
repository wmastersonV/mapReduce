#!/usr/bin/python

# given features, what is the probability of Y?
# p(Y | x) ~ p(x | Y) p(Y) / [ p(x | Y) p(Y) + p(x | not-Y) p(not-Y)]
# this mapper emits tuples that are used for predictions on a pre-specified feature set
# testfile | ./mapper.py

import sys
import pandas as pd
import numpy as np

dfY = pd.read_csv("naiveBayes/trainDependant.csv", sep = "\t")
dfX = pd.read_csv("naiveBayes/trainIndependant.csv", sep = "\t")

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








