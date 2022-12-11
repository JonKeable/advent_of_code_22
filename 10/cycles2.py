
f = open("input.txt", 'r')
lineList = f.read().splitlines()

insList = [line.split() for line in lineList]

for ins in insList:
    if len(ins) > 1:
        ins[1] = int(ins[1])

#inits
reg = 1
cycle = 1
values = {}
i=0

while i < len(insList) :
    #print(i)
    values[cycle] = reg
    #print (reg)
    cycle += 1
    if insList[i][0] == 'noop':
        pass
    elif insList[i][0] == 'addx':
        values[cycle] = reg
        print("addx " + str(insList[i][1]))
        reg += insList[i][1]
        cycle += 1
    i+=1
    #print(i)
    
    
#print(insList)
print(values)

#multKeys = {k for k in values.keys() if ((k +20) % 40) == 0}

crt = [0] * 240

def printCRT(crt) :
    for j in range(6):
        print(crt[40*j:40*j+40])

#printCRT(crt)

for key in sorted(list(values.keys())):
    modKey = (key-1) % 40
    if values[key] in range(modKey-1, modKey+2) :
        crt[key-1] = '#'
    else:
        crt[key-1] = '.'


printCRT(crt)
#print(crt)