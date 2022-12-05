f = open("input.txt", 'r')
lineList = f.read().splitlines()

#print(lineList)

pairList = [tuple(pair.split(',')) for pair in lineList]

#print(pairList)

def geRangeTuple(rangeStr) :
    tup = tuple(rangeStr.split('-'))
    return tuple([int(x) for x in tup])

rangeList = [(geRangeTuple(rangeStr[0]), geRangeTuple(rangeStr[1])) for rangeStr in pairList]

print(rangeList)

def isSubset(p):
    #print (f'{a} and {b}')
    a = p[0]
    b = p[1]
    isSubset = False
    if not(a[0] > b[1] or b[0] > a[1]) :
        isSubset = True

    #print(isSubset)
    #print()
    return isSubset

subsetsList = [isSubset(pair) for pair in rangeList]





# print(subsetsList)

print(subsetsList.count(True))

# print(rangeList[1])

# print(isSubset(((9,69),(14,70))))

# print(len(subsetsList))


# count=0
# for pair in rangeList :
#     if isSubset(pair) :
#         print(pair)
#         count +=1
# print(count)