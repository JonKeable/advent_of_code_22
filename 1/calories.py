import this


f = open("input.txt", 'r')
lineList = f.read().splitlines()
#print(lineList)

intList = ['#' if e == '' else int(e) for e in lineList]
intList.append('#')
print(intList)
maxCal = 0
thisCal = 0
for e in intList:

    if e == '#':
        #print('new elf')
        #print(thisCal)
        #print(maxCal)
        #print('---')
        if thisCal > maxCal:
            maxCal = thisCal
        thisCal = 0
    else:
        #print(e)
        thisCal += e
        #print(e)
        #print(thisCal)

print(maxCal)