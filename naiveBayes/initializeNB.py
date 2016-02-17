import pandas as pd
import pdb
import numpy

# bin features and dependant variable for naive bayes algo
def binDF(x):
    if type(x) is str:
        return x
    else:
        bins = numpy.linspace(x.min(), x.max(), 3)
        groups = pd.cut(x, bins)
        return groups

fp = "linearReg/train.csv"
df = pd.read_csv(fp)
print(df.columns)
# pdb.set_trace()
dfOut = df[['P1', 'P2', 'P3', 'P4', 'revenue']]

dfOut2 = dfOut.apply(binDF)
dfOut2[['revenue']].to_csv("naiveBayes/trainDependant.csv", sep='\t', index = False )
dfOut2[['P1', 'P2', 'P3', 'P4']].to_csv("naiveBayes/trainIndependant.csv", sep='\t', index = False )

