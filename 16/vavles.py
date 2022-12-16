import re
import networkx as nx
import matplotlib.pyplot as plt

def splitValve(coList):
    return {'V' : coList[0], 'F': coList[1], 'T': coList[2:]}

f = open('test.txt', 'r')

lineList = f.read().splitlines()

# regex to get the coords only from each line
pattern = '[A-Z]{2}|\d+'

valveList = [splitValve(re.findall(pattern, line)) for line in lineList]

G = nx.Graph()

for valve in valveList:
    print(valve)
    G.add_node(valve['V'], attr_dict={'F' : valve['F']})

for valve in valveList:
    for con in valve['T']:
        G.add_edge(valve['V'], con)

nx.draw_networkx(G)
plt.show()
