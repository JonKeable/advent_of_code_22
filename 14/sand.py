def printLines(list):
    [print(line) for line in list]

def printgrid(g) :
    print("\n--------------------\n")
    for row in g :
        line = ''
        for e in row:
            line += ' ' + str(e) + ' '
        print(line)
        

def dropSand(grid, xOff, point):
    x = point[0]
    y = point[1]
    if y >= maxY:
        return False
    elif grid[y+1][x-xOff] == '.':
        return dropSand(grid, xOff, (x, y+1))
    elif x <= minX:
        return False
    elif grid[y+1][x-xOff-1] == '.':
        return dropSand(grid, xOff, (x-1, y+1))
    elif x >= maxX:
        return False
    elif grid[y+1][x-xOff+1] == '.':
        return dropSand(grid, xOff, (x+1, y+1))
    elif grid[y][x-xOff] != '+':
        grid[y][x-xOff] = 'o'
        return True
    else:
        return False        

f = open('input.txt', 'r')

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
#printgrid(grid)

for path in rockList:
    start = path[0]
    for point in path:
        #abs magic to do inclusive for both negative and positive differences
        dX = point[0] - start[0]
        dY = point[1] - start[1]
        stepX = -1 if dX<0 else 1
        stepY = -1 if dY<0 else 1
        for x in range(start[0], point[0] + stepX, stepX):
            for y in range(start[1], point[1] + stepY, stepY):
                grid[y][x-minX] = '#'
        start = point

#printgrid(grid)

source = (500, 0)
settled = 0
canSettle = True

while(canSettle):
    canSettle = dropSand(grid, minX, source)
    if canSettle:
        settled += 1
        #printgrid(grid)

#printgrid(grid)
print(settled)