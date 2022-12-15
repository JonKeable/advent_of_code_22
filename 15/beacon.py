import re

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

f = open('test.txt', 'r')

lineList = f.read().splitlines()

# regex to get the coords only from each line
pattern = '\d+'

coordList = [splitCoords(listToInt(re.findall(pattern, line))) for line in lineList]

print(coordList)

for coords in coordList:
    s = coords['S']
    b = coords['B']
    d = abs(s[0] -b[0]) + abs(s[1] - b[1])
    coords['D'] = d

print(coordList)

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
grid = [['.' for _ in range(minX, maxX)] for _ in range(minY,maxY)]

#init signal and beacon positions
for c in coordList:
    s = c['S']
    b = c['B']
    grid[s[1]-minY][s[0]-minX] = 'S'
    grid[b[1]-minY][b[0]-minX] = 'B'

printgrid(grid)

for c in coordList:
    s = c['S']
    d = c['D']

    for y in range(s[1]-d, s[1]+d+1):
        xLow = s[0]-d
        xHigh = s[0]+d+1 
        mod= abs(s[1]-y)
        for x in range(xLow+mod, xHigh-mod):
            if grid[y-minY][x-minX] == '.':
                grid[y-minY][x-minX] = '#'
    printgrid(grid)
