def touching (h,t) :
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) <2
  

def move(dir, k):

    if dir == 'R':
        doMove(1, 'x', k)
    elif dir == 'L':
        doMove(-1, 'x', k)
    elif dir =='U':
        doMove(1, 'y', k)
    else:
        doMove(-1, 'y', k)
    return 0


def doMove(d, ax, k):
    a = 0 if ax == 'x' else 1
    b = 0 if ax == 'y' else 1
    for _ in range(k) :
        head[a] += d
        if not touching(head, tail):
            if head[a] != tail[a] :
                tail[a] += d
                if head[b] != tail[b]:
                    tail[b] = head[b]
            #print(tail)
            visited.add(tuple(tail))
            


f = open("test2.txt", 'r')
lineList = f.read().splitlines()

moveList = [(line.split()[0], int(line.split()[1])) for line in lineList]

print (moveList)

head = [0, 0]
tail = [0, 0]
visited = set()
visited.add(tuple(tail))

for m in moveList:
    move(m[0], m[1])

print(visited)
print (len(visited))
