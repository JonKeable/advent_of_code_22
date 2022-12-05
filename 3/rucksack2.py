f = open("input.txt", 'r')
lineList = f.read().splitlines()

print(lineList)

pDict = {}


def popDict(d, sc, sn):
    for i in range(26) :
        pDict[sc] = i+sn
        sc = chr(ord(sc) + 1)

popDict(pDict, 'a', 1)
popDict(pDict, 'A', 27)

#print(pDict)

#works assuming bags contain even numbers of items

groupList = []
groupSize = 3
for i in range(0, len(lineList), groupSize):
    groupList.append(lineList[i:i+groupSize])

print(groupList)

def getShared(elves):
    sharedSet = set(elves[0])
    for elf in elves :
        sharedSet = sharedSet & set(elf)
    return sharedSet.pop()

badgeList = [getShared(group) for group in groupList]

print(badgeList)


pList = [pDict[badge] for badge in badgeList]

print(sum(pList))
