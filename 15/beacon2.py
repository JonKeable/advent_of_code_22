import re
from bitarray import bitarray
from threading import Thread



def splitCoords(coList):
    return {'S' : coList[:2], 'B': coList[2:]}

def listToInt(l):
    return [int(s) for s in l]

def printgrid(g) :
    print("\n--------------------\n")
    fl = '   '
    for i in range(minX, maxX):
        if i > -1 and i < 10:
            fl +=  ' ' + str(i) + ' '
        else :
            fl += str(i) + ' ' 
    print(fl)
    for index, row in enumerate(g) :
        
        line = f'{index + minY:>3}'
        for e in row:
            line += ' ' + str(e) + ' '
        print(line)

def computeSignal(c):
    s = c['S']
    d = c['D']
    xLow = s[0]-d
    xHigh = s[0]+d+1 

    for y in range(s[1]-d, s[1]+d+1):
        mod= abs(s[1]-y)
        if y >= min and y <=max and xLow+mod >= min and xHigh+mod <=max:

            #for x in range(xLow+mod, xHigh-mod):
            #    scanned.add((x,y))
            # scanned = scanned | set([(x,y) for x in range(xLow+mod,xHigh-mod)])
            
            scanned.add((xLow+mod, y))
            scanned.add((xHigh-mod, y))




f = open('input.txt', 'r')

lineList = f.read().splitlines()

# regex to get the coords only from each line
pattern = '-*\d+'

coordList = [splitCoords(listToInt(re.findall(pattern, line))) for line in lineList]

#print(coordList)

for coords in coordList:
    s = coords['S']
    b = coords['B']
    d = abs(s[0] -b[0]) + abs(s[1] - b[1])
    coords['D'] = d

#print(coordList)


#targetRow = 2000000
min = 0
max = 4000000
scanned = set()
#all = {(x,y) for x in range(min, max+1) for y in range(min, max)}

validRows = {}

threads = []

for c in coordList:
    s = c['S']
    print(f'signal @ {s}')
    t= Thread(target=computeSignal, args=(c,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print(len(scanned))


