f = open("input.txt", 'r')
lineList = f.read().splitlines()

#print(lineList)

#works assuming bags contain even numbers of items
compList = [(bag[:len(bag)//2], bag[len(bag)//2:]) for bag in lineList]

#print(compList)

sharedList = [(set(comp[0]) & set(comp[1])).pop() for comp in compList]

print(sharedList)

pDict = {}


def popDict(d, sc, sn):
    for i in range(26) :
        pDict[sc] = i+sn
        sc = chr(ord(sc) + 1)

popDict(pDict, 'a', 1)
popDict(pDict, 'A', 27)

print(pDict)

pList = [pDict[item] for item in sharedList]

print(sum(pList))
