f = open('input.txt', 'r')

data = f.readline()

for i,c in enumerate(data):
    if len(set(data[i:i+4])) == 4 :
        print (i+4)
        print(data[i:i+4])
        break