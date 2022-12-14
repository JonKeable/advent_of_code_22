def printLines(list):
    [print(line) for line in list]

f = open('test.txt', 'r')

lineList = f.read().splitlines()

rockList = [line.split(' -> ') for line in lineList]

printLines(rockList)