def touching(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def move(dir, k):
    #print("move: " + dir + " " + str(k))
    for _ in range (k) :
        if dir == 'R':
            rope[0][0] += 1
        elif dir == 'L':
            rope[0][0] -= 1
        elif dir == 'U':
            rope[0][1] += 1
        elif dir == 'D':
            rope[0][1] -= 1
        doMove(0)
    return


def doMove(i):
        head = rope[i]
        tail = rope[i+1]
        newTail = tail.copy()
        if not touching(head, tail):
            dx = head[0] - tail[0]
            dy = head[1] - tail[1]
            if dx != 0:
                newTail[0] += dx // abs(dx)
            if dy !=0:
                newTail[1] += dy // abs(dy)
            rope[i+1] = newTail
            if i < len(rope) - 2:
                doMove(i+1)
            else:
                #print('tail: ' + str(tail))
                visited.add(tuple(newTail))
                #print('tail: ' + str(newTail))        
                


f = open("input.txt", 'r')
lineList = f.read().splitlines()

moveList = [(line.split()[0], int(line.split()[1])) for line in lineList]

print(moveList)

ropeLength = 10

rope = [[0, 0] for _ in range(ropeLength)]
print(rope)
print(rope[0])
visited = set()
visited.add((0, 0))

for m in moveList:
    move(m[0], m[1])
    #print (rope)

print(visited)
print(rope)
print(len(visited))
