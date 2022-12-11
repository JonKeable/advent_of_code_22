from collections import deque

class Monkey:
    def __init__ (self, id, startingItems, operation, test, t, f):
        self.id = int(id.split()[1].replace(':', ''))
        self.startingItems = startingItems.split()[2:]
        startingItems = [int(e.replace(',','')) for e in self.startingItems]
        self.currentItems = deque()
        for e in startingItems :
            self.currentItems.append(e)
        opList = operation.split()
        self.operand =  opList[4]
        self.opX = opList[5]
        testList = test.split()
        self.testType = testList[1]
        self.testX = testList[3]
        self.trueMonkey = int(t.split()[-1])
        self.falseMonkey = int(f.split()[-1])

    def __str__(self) -> str:
        return("Monkey " + str(self.id) + ':')


