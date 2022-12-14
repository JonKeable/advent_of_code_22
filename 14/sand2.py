def printLines(list):
    [print(line) for line in list]

def printgrid(g) :
    print("\n--------------------\n")
    for row in g :
        line = ''
        for e in row:
            line += ' ' + str(e) + ' '
        print(line)
        

def dropSand(grid, min, max, point):
    x = point[0]
    y = point[1]
    if y >= max:
        return False
    elif grid[y+1][x-min] == '.':
        return dropSand(grid, min, max, (x, y+1))
    elif x <= min:
        return False
    elif grid[y+1][x-min-1] == '.':
        return dropSand(grid, min, max, (x-1, y+1))
    elif x >= max:
        return False
    elif grid[y+1][x-min+1] == '.':
        return dropSand(grid, min, max, (x+1, y+1))
    elif grid[y][x-min] in ['.', '+']:
        grid[y][x-min] = 'o'
        return True
    else:
        return False        

f = open('input.txt', 'r')

lineList = f.read().splitlines()

rockList = [line.split(' -> ') for line in lineList]

#printLines(rockList)

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

floorY =  maxY + 2
maxY = floorY

grid = [[] for _ in range(minY, maxY+1)]

min = 500 - floorY
max = 500 + floorY

for row in grid:
    row.extend(['.' for _ in range(min, max+1)])

grid[0][500-min] = '+'
grid[maxY] = ['#']*(len(grid[0]))
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
                grid[y][x-min] = '#'
        start = point

#printgrid(grid)

source = (500, 0)
settled = 0
canSettle = True

while(canSettle):

    canSettle = dropSand(grid, min, max, source)
    if canSettle:
        settled += 1
        if settled %1000 == 0:
            print (settled)
        #printgrid(grid)


#printgrid(grid)
print(settled)