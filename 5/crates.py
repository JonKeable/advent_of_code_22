import pandas as pd

f = open("input.txt", 'r')
lineList = f.read().splitlines()

#print(lineList)

stacks = [[] for _ in range(9)] 
print('stackS:')
print(stacks)
print(stacks[4])

stackInput = lineList[:8]
print(stackInput)

def pushData(line):
    for i in range(len(line)//4 + 1) :
        #print(i)
        loc = i * 4
        val = line[loc+1]
        #print(val)
        if val != ' ':
            stacks[i].append(val)

for line in stackInput:
    pushData(line)

print('-----------------')
print(stacks)

for stack in stacks :
    stack.reverse()

print('-----------------')
print(stacks)

moves = lineList[10:]

print(moves[:10])
print(moves[-10:])

moves = [move.split() for move in moves]

print (moves[:10])

def makeMove(move) :
    k = int(move[1])
    fr = int(move[3])-1
    to = int(move[5])-1
    for i in range (k) :
        stacks[to].append(stacks[fr].pop())

for move in moves :
    print(move)
    makeMove(move)
    print(stacks)

print(stacks)

topCrates = ''

for stack in stacks :
    topCrates += stack.pop()

print(topCrates)
