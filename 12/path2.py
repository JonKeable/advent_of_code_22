import networkx as nx
import matplotlib.pyplot as plt
#import scipy

def printLines(list):
    [print(line) for line in list]

def inBounds(row, col) :
    # is this more efficient than ands?
    return not (row < 0 or row >= height or col < 0 or col >= width)

G = nx.DiGraph()

f = open('input.txt', 'r')
lineList = f.read().splitlines()
lineList.append('')

printLines(lineList)

grid =[[ord(c) for c in line] for line in lineList]

if grid[len(grid)-1] == []:
    grid.pop() 


end = ()
starts=[]

height = len(grid)
width = len(grid[0])

#populate graph from input
for row, line in enumerate(grid):
    #print(row)
    for col, char in enumerate(line):
        if char == ord('a'):
            starts.append((row,col))
        if char == 83:
            # start = (row, col)
            #elev a
            grid[row][col] = ord('a')
        elif char == 69:
            end = (row, col)
            #elev z
            grid[row][col] = ord('z')
        G.add_node((row,col))

#nx.draw_networkx(G)
#plt.show()

for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if col > 0:
            if char - grid[row][col-1] >= -1:
                G.add_edge((row,col), (row, col-1))
        if col < width - 1:
            if char - grid[row][col+1] >= -1:
                G.add_edge((row,col), (row, col+1))

        if row > 0:
            if char - grid[row-1][col] >= -1:
                G.add_edge((row,col), (row-1, col))
        if row < height - 1:
            if char - grid[row+1][col] >= -1:
                G.add_edge((row,col), (row+1, col))
        

#nx.draw_networkx(G)

#path = nx.astar_path(G, start, end)


#print(path)5
pathLens = []

for start in starts:
    try:
        pl = nx.astar_path_length(G, start, end)
        pathLens.append(nx.astar_path_length(G, start, end))
        #print(pl)
    except:
        pass

print(sorted(pathLens)[0])

#plt.show()