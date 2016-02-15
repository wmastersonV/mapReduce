import pandas as pd
# test
fp = "/Users/dallammasterson/gitRepos/mapReduce/linearReg/train.csv"
df = pd.read_csv(fp)
print(df.columns)
dfOut = df[['P1', 'P2', 'P3', 'P4', 'revenue']]
dfOut.to_csv("/Users/dallammasterson/gitRepos/mapReduce/linearReg/trainNew.csv", sep='\t', index = False )

