import this


f = open("input.txt", 'r')
lineList = f.read().splitlines()
#print(lineList)

intList = ['#' if e == '' else int(e) for e in lineList]
intList.append('#')
print(intList)
maxCal = [0,0,0]
thisCal = 0
for e in intList:

    if e == '#':

        print(thisCal)
        for i, e in enumerate(maxCal):
            if thisCal > e:
                maxCal[i] = thisCal
                break

        thisCal = 0
    else:
        #print(e)
        thisCal += e


print(maxCal)
print(sum(maxCal))