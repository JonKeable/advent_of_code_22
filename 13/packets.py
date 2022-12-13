import numpy as np

def printLines(list):
    [print(line) for line in list]

def compare(pair):
    left = pair[0]
    right = pair[1]


f = open('test.txt', 'r')
lineList = f.read().splitlines()
lineList.append('')

#printLines(lineList)

pairList = np.array_split(lineList, len(lineList) // 3)

pairList = [arr.tolist()[:2] for arr in pairList]

pairList = [(eval(pair[0]), eval(pair[1])) for pair in pairList]

printLines(pairList)