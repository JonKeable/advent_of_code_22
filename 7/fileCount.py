import re
f = open("input.txt", "r")
lineList = f.read().splitlines()

cmdList = [line.split() for line in lineList]

print(cmdList)

sum = 0

for cmd in cmdList:
    if re.match(r"\d+", cmd[0]):
        sum += int(cmd[0])

print(f'whole dir: {sum}')