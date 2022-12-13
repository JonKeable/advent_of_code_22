import numpy as np

def printLines(list):
    [print(line) for line in list]

def compare(pair):
    left = pair[0]
    right = pair[1]

    leftIsInt = isinstance(left, int)
    rightIsInt = isinstance(right, int)

    if leftIsInt and rightIsInt:
        valid = right - left
        if valid > 0:
            return True
        elif valid < 0:
            return False
        else:
            return None
    
    elif leftIsInt:
        left = [left]
    
    elif rightIsInt:
        right = [right]

    lenLeft = len(left)
    for i, val in enumerate(right):
        if i < lenLeft:
            valid = compare((left[i],val))
            if valid != None:
                return valid
        else:
            return True
            
    
    if lenLeft > len(right):
        return False
    else:
        return None



f = open('test.txt', 'r')
lineList = f.read().splitlines()
lineList.append('')

#printLines(lineList)

pairList = np.array_split(lineList, len(lineList) // 3)

pairList = [arr.tolist()[:2] for arr in pairList]

pairList = [(eval(pair[0]), eval(pair[1])) for pair in pairList]

printLines(pairList)

validList =[]

for pair in pairList:
    validList.append(compare(pair))

print (validList)