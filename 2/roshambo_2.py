import networkx  as nx
import numpy as np
import matplotlib.pyplot as plt

f = open("input.txt", 'r')
lineList = f.read().splitlines()
#print(lineList)

tupleList = [tuple(line.split()) for line in lineList]

print(tupleList)

scoreDict = {'A' : 1, 'B' : 2, 'C' : 3}
resDict = {'W' : 6, 'D' : 3, 'L' : 0}
charDict = {'X' : 'L', 'Y' : 'D', 'Z' : 'W'}
options = ['A', 'B', 'C']

winG = nx.DiGraph()
for l in options :
    winG.add_node(l)

winG.add_edge('A', 'C')
winG.add_edge('B', 'A')
winG.add_edge('C', 'B')

nx.draw_networkx(winG)
#plt.show()

print(next(winG.successors('A')))

def getScore (round) :
    opp = round[0]
    meCode = round[1]
    res = charDict[meCode]
    me = ''
    if res == 'D' :
        me = opp
    else :
        if res == 'L' :
           me = next(winG.successors(opp))
        else :
            me = next(winG.successors(next(winG.successors(opp))))

    value = scoreDict[me]
    score = value + resDict[res]
    return score
        
roundScores = [getScore(round) for round in tupleList]
print(roundScores)
print(sum(roundScores))    



