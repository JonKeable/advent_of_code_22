
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
    if insList[i][0] == 'noop':
        cycle += 1
    elif insList[i][0] == 'addx':
        cycle += 1
        values[cycle] = reg
        print("addx " + str(insList[i][1]))
        reg += insList[i][1]
        cycle += 1
    i+=1
    #print(i)
    
    
#print(insList)
print(values)

multKeys = {k for k in values.keys() if ((k +20) % 40) == 0}

sum = 0
for key in multKeys:
    sum += key * values[key]

print (sum)