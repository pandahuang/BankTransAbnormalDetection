__author__ = 'panda'
import networkx as nx
import matplotlib.pyplot as plt

GraphFilePATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphFile.txt"
GraphFilePATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphFile.txt"

Edges = []
CentreNode = []
LoadNum = 0
LoadMax = 1
with open(GraphFilePATH) as fopen:
    Lines = fopen.readlines()
    for line in Lines:
        edge = line.strip().split('\t')
        if len(edge) == 1 and LoadNum < LoadMax:
            LoadNum = LoadNum + 1
            CentreNode.append(line.strip())
        elif len(edge) == 2 and LoadNum <= LoadMax:
            Edges.append(line.strip())
        else:
            break

G = nx.DiGraph()
for edge in Edges:
    SNode = edge.split('\t')[0]
    DNode = edge.split('\t')[1]
    G.add_edge(SNode, DNode)

GRAPHCYCLEPATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphCycle.txt"
CycleList = list(nx.simple_cycles(G))
with open(GRAPHCYCLEPATH, 'w') as fopen:
    for line in CycleList:
        fopen.write(line)
        fopen.write('\n')

GRAPHDEGREEPATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphDegree.txt"
DegreeList = nx.degree(G)
with open(GRAPHDEGREEPATH, 'w') as fopen:
    for line in DegreeList:
        fopen.write(line)
        fopen.write('\n')

# nx.draw_networkx(G, pos=nx.random_layout(G), arrows=False, node_size = 10, with_labels=False, width=0.2)
# plt.savefig("G:\\projects\\FraudDetection\\Data\\GraphData\\GraphPic.png")
# plt.show()

