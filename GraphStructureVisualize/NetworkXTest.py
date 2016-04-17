__author__ = 'panda'
import networkx as nx
import matplotlib.pyplot as plt

GraphFilePATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphFile.txt"
GraphFilePATH = "G:\\projects\\FraudDetection\\Data\\GraphData\\GraphFile.txt"

Edges = []
CentreNode = []
LoadNum = 0
LoadMax = 2
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
# for node in CentreNode:
#     G.add_node(node)
for edge in Edges:
    SNode = edge.split('\t')[0]
    DNode = edge.split('\t')[1]
    G.add_edge(SNode, DNode)

nx.draw_networkx(G, pos=nx.random_layout(G), arrows=False, node_size = 10, with_labels=False, width=0.2)
plt.savefig("G:\\projects\\FraudDetection\\Data\\GraphData\\GraphPic.png")
plt.show()

