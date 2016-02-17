# mapReduce
built using python 3

example ml algos written in map reduce paradigm

This code is stand alone and does not require the udacity VM with map reduce installed.

to run, cd into the respective sub-folder and type this into terminal:
'cd mapReduce/<algo>/'
python3 mapper.py | sort | ./reducer.py

location of the map reduce virtual machine download from Udacity:
https://docs.google.com/document/d/1v0zGBZ6EHap-Smsr3x3sGGpDW-54m82kDpPKC2M6uiY/pub?embedded=true

to run in Hadoop:
hs mapper.py reducer.py inputFolder outputFolder

