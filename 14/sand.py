def printLines(list):
    [print(line) for line in list]

def printgrid(g) :
    print("\n--------------------\n")
    for row in g :
        line = ''
        for e in row:
            line += ' ' + str(e) + ' '
        print(line)
        

f = open('test.txt', 'r')

lineList = f.read().splitlines()

rockList = [line.split(' -> ') for line in lineList]

printLines(rockList)

for path in rockList:
    for i, point in enumerate(path):
        path[i] = eval('(' + point + ')')

minX = 500
minY = 0
maxX = 0
maxY = 0

for path in rockList:
    for i, point in enumerate(path):  
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])
        minX = min(minX, point[0])

grid = [[] for _ in range(minY, maxY)]

for row in grid:
    row.extend(['.' for _ in range(minX, maxX)])

printgrid(grid)

