import numpy as np
from packet import Packet

def printLines(list):
    [print(line) for line in list]


f = open('input.txt', 'r')
lineList = f.read().splitlines()
inputList =[eval(line) for line in lineList if line != '']


inputList = [[[2]]] + inputList + [[[6]]]
inputList = [Packet(e) for e in inputList]

printLines(inputList)

sortedPackets = sorted(inputList)

print('------------------------\n')

printLines(sortedPackets)

key = (sortedPackets.index(Packet([[2]]))+1) * (sortedPackets.index(Packet([[6]]))+1)

print (f'key = {key}')
