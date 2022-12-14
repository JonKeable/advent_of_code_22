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

grid = [[] for _ in range(minY, maxY+1)]

for row in grid:
    row.extend(['.' for _ in range(minX, maxX+1)])

grid[0][500-minX] = '+'
printgrid(grid)

for path in rockList:
    start = path[0]
    for point in path:
        #abs magic to do inclusive for both negative and positive differences
        dX = point[0] - start[0]
        dY = point[1] - start[1]
        stepX = dX//abs(dX) if dX !=0 else 1
        stepY = dY//abs(dY) if dY !=0 else 1
        for x in range(start[0], point[0] + stepX, stepX):
            for y in range(start[1], point[1] + stepY, stepY):
                grid[y][x-minX] = '#'
        start = point

printgrid(grid)