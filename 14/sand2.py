def printLines(list):
    [print(line) for line in list]

def printgrid(g):
    print("\n--------------------\n")
    for row in g:
        line = ""
        for e in row:
            line += " " + str(e) + " "
        print(line)

""" try to drop a grain of sand one tile
 omit in-bounds checks as we made the grid oversized
 return true if there is space for the sand to settle.
 otherwise return false"""
def dropSand(grid, min, max, point):
    x = point[0]
    y = point[1]
    if grid[y + 1][x - min] == ".":
        return dropSand(grid, min, max, (x, y + 1))
    elif grid[y + 1][x - min - 1] == ".":
        return dropSand(grid, min, max, (x - 1, y + 1))
    elif grid[y + 1][x - min + 1] == ".":
        return dropSand(grid, min, max, (x + 1, y + 1))
    elif grid[y][x - min] in [".", "+"]:
        grid[y][x - min] = "o"
        return True
    else:
        return False

# read data
f = open("input.txt", "r")
lineList = f.read().splitlines()
rockList = [line.split(" -> ") for line in lineList]
for path in rockList:
    for i, point in enumerate(path):
        path[i] = eval("(" + point + ")")

# figure out how big the grid needs to be
minX = 500
minY = 0
maxX = 0
maxY = 0

for path in rockList:
    for i, point in enumerate(path):
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])
        minX = min(minX, point[0])

floorY = maxY + 2
maxY = floorY

# create grid rows(y)
grid = [[] for _ in range(minY, maxY + 1)]

# make the grid at least wide enough for a pyramid going one out each row,
# with some room to spare
minX = 500 - floorY - 100
maxX = 500 + floorY + 100

# create empty grid
for row in grid:
    row.extend(["." for _ in range(minX, maxX + 1)])

# add the source
grid[0][500 - minX] = "+"
# add the floor
grid[maxY] = ["#"] * (len(grid[0]))

# add rock paths
for path in rockList:
    start = path[0]
    for point in path:
        # get path direction for each axis
        dX = point[0] - start[0]
        dY = point[1] - start[1]
        stepX = -1 if dX < 0 else 1
        stepY = -1 if dY < 0 else 1
        for x in range(start[0], point[0] + stepX, stepX):
            for y in range(start[1], point[1] + stepY, stepY):
                # offset the x by the x origin of the grid
                grid[y][x - minX] = "#"
        start = point


print("...")
# try to settle the sand from source, count how many grains can settle
source = (500, 0)
settled = 0
canSettle = True
while canSettle:
    canSettle = dropSand(grid, minX, maxX, source)
    if canSettle:
        settled += 1
        # printgrid(grid)


# printgrid(grid)
print(settled)
