from monkey import Monkey
import numpy as np


def takeTurn(monkey, list, mod):
    while (monkey.currentItems):
        result = monkey.inspect(mod)
        list[result[0]].addItem(result[1])


f = open('input.txt', 'r')
lineList = f.read().splitlines()
lineList.append('')

print(lineList)

monkeyList = np.array_split(lineList, len(lineList) // 7)

monkeyList = [arr.tolist() for arr in monkeyList]


for l in monkeyList:
    l.pop()

print(monkeyList)

monkeyList = [Monkey(m[0], m[1], m[2], m[3], m[4], m[5]) for m in monkeyList]


def printMonkeys(list):
    for monkey in list:
        print(monkey)

modulo = 1
divSet = set()
for monkey in monkeyList:
    divSet.add(monkey.testX)

for d in divSet:
    modulo *= d

print(modulo)

numberOfRounds = 10000
for round in range(1, numberOfRounds+1):
    for monkey in monkeyList:
        takeTurn(monkey, monkeyList, modulo)


printMonkeys(monkeyList)

inspectionsCounts = sorted([monkey.inspections for monkey in monkeyList], reverse=True)

print(inspectionsCounts)

monkeyBusiness = inspectionsCounts[0] * inspectionsCounts[1]

print(monkeyBusiness)


