__author__ = 'panda'
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
for i in range(100):
    if i < 100:
        G.add_edge(i,i+2)
    else:
        G.add_edge(i+1,0)
nx.draw_networkx(G, pos=nx.spring_layout(G), arrows=False, node_size = 10, with_labels=False)
plt.savefig("D:\\G.png")