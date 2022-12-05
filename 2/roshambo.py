import networkx  as nx
import numpy as np
import matplotlib.pyplot as plt

f = open("input.txt", 'r')
lineList = f.read().splitlines()
#print(lineList)

tupleList = [tuple(line.split()) for line in lineList]

print(tupleList)

scoreDict = {'X' : 1, 'Y' : 2, 'Z' : 3}
resDict = {'W' : 6, 'D' : 3, 'L' : 0}
charDict = {'X' : 'A', 'Y' : 'B', 'Z' : 'C'}
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
    res = ''
    value = scoreDict[meCode]
    me = charDict[meCode]
    if opp == me :
        res = 'D'
    else :
        if next(winG.successors(opp)) == me :
            res = 'L'
        else :
            res = 'W'

    score = value + resDict[res]
    return score
        
roundScores = [getScore(round) for round in tupleList]
print(roundScores)
print(sum(roundScores))    



