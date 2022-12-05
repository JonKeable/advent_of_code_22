import this


f = open("input.txt", 'r')
lineList = f.read().splitlines()
#print(lineList)

intList = ['#' if e == '' else int(e) for e in lineList]
intList.append('#')
#print(intList)
elfList = []
thisCal = 0
thisElf = []

for e in intList:

    if e == '#':
        elfList.append(thisElf)
        thisElf= []
    else:
        thisElf.append(e)


#print(elfList)

calList = [sum(elf) for elf in elfList]

print(calList)

calList.sort(reverse=True)

print(calList)

topThree = calList[:3]
print(topThree)
print(sum(topThree))
