import re
from scipy.sparse import lil_matrix
import numpy as np

def splitCoords(coList):
    return {'S' : coList[:2], 'B': coList[2:]}

def listToInt(l):
    return [int(s) for s in l]

def printgrid(g) :
    print("\n--------------------\n")
    for row in g :
        line = ''
        for e in row:
            line += ' ' + str(e) + ' '
        print(line)

f = open('input.txt', 'r')

lineList = f.read().splitlines()

# regex to get the coords only from each line
pattern = '\d+'

coordList = [splitCoords(listToInt(re.findall(pattern, line))) for line in lineList]

#print(coordList)

for coords in coordList:
    s = coords['S']
    b = coords['B']
    d = abs(s[0] -b[0]) + abs(s[1] - b[1])
    coords['D'] = d

#print(coordList)

minX = coordList[0]['S'][0]
minY = coordList[0]['S'][1]
maxX = minX
maxY = minY


for c in coordList:
    s = c['S']
    d = c['D']
    minX = min(s[0]-d, minX)
    minY = min(s[1]-d, minY)
    maxX = max(s[0]+d, maxX)
    maxY = max(s[1]+d, maxY)

minY -= 1
maxY += 2
minX -= 1
maxX += 2

#empty grid
'''grid = [[] for _ in range(minY,maxY)]
emptyRow = bytearray([0 for _ in range(minX, maxX)])
for i, _ in enumerate(grid):
    grid[i] = emptyRow.copy()'''

#grid = lil_matrix((maxY-minY, maxX-minX), dtype=np.int8)

targetRow = 2000000
scanned = set()

#printgrid(grid)

for c in coordList:
    s = c['S']
    d = c['D']
    xLow = s[0]-d
    xHigh = s[0]+d+1 
    print(f'signal @ {s}')

    for y in range(s[1]-d, s[1]+d+1):
        if y == targetRow:

            mod= abs(s[1]-y)
            #for x in range(xLow+mod, xHigh-mod):
            #    grid[y-minY,x-minX] = 1
            #yC = y-minY
            xLow = xLow + mod
            xHigh = xHigh - mod
            #grid[yC, xLow:xHigh] = 1
            scanned = scanned | set([x for x in range(xLow,xHigh)]) 

        
        #print(grid[y-minY, xLow+mod:xHigh-mod])
        #print()
    #printgrid(grid.toarray())

#add known beacon positions
for c in coordList:
    s = c['S']
    b = c['B']
    #grid[s[1]-minY,s[0]-minX] = 0
    #grid[b[1]-minY,b[0]-minX] = 0
    if s[1] == targetRow and s[0] in scanned:
        scanned.remove(s[0])
    if b[1] == targetRow and b[0] in scanned:
        scanned.remove(b[0])
#printgrid(grid)

print(scanned)
print(len(scanned))

#printgrid(grid.toarray())
#print(grid.getrow(10-minY).toarray())
