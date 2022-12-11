from collections import deque

class Monkey:
    def __init__ (self, id, startingItems, operation, test, t, f):
        self.id = int(id.split()[1].replace(':', ''))
        startingItems = startingItems.split()[2:]
        startingItems = [int(e.replace(',','')) for e in startingItems]
        self.currentItems = deque()
        for e in startingItems :
            self.currentItems.append(e)
        opList = operation.split()
        self.operand =  opList[4]
        self.opX = opList[5]
        testList = test.split()
        self.testType = testList[1]
        self.testX = int(testList[3])
        self.trueMonkey = int(t.split()[-1])
        self.falseMonkey = int(f.split()[-1])
        self.inspections = 0

    def __str__(self) -> str:
        return("Monkey " + str(self.id) + ': ' + str(self.currentItems) 
        + "\n" + str(self.inspections) + " inspections")

    def popItem(self):
        return self.currentItems.popleft()

    def addItem(self, item):
        self.currentItems.append(item)

    def inspect(self) :
        self.inspections += 1
        item = self.popItem()
        opX = item if self.opX == 'old' else int(self.opX)
        worryLevel = 0
        if self.operand == '*':
            worryLevel = item * opX
        elif self.operand == '+':
            worryLevel = item + opX
        worryLevel  = worryLevel // 3
        if worryLevel % self.testX == 0:
            return (self.trueMonkey, worryLevel)
        else:
            return (self.falseMonkey, worryLevel)
    

    
