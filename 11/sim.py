from monkey import Monkey
import numpy as np

f = open("input.txt", 'r')
lineList = f.read().splitlines()
lineList.append('')

print(lineList)

monkeyList = np.array_split(lineList, len(lineList) // 7)

monkeyList = [arr.tolist() for arr in monkeyList]


for l in monkeyList:
    l.pop()

print(monkeyList)

monkeyList = [Monkey(m[0], m[1], m[2],m[3],m[4],m[5]) for m in monkeyList]

for monkey in monkeyList:
    print (monkey)