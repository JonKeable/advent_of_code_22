f = open('input.txt', 'r')

data = f.readline()

def printStartStr(data, k):
    for i,c in enumerate(data, k):
        if len(set(data[i:i+k])) == k :
            print (i+k)
            print(data[i:i+k])
            break

printStartStr(data, 14)