import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
with open('in.txt') as input_file:
    for row in csv.reader(input_file, delimiter=")"):
        G.add_nodes_from(row)
        G.add_edges_from([row])

print(sum([len(nx.ancestors(G, n)) for n in G.nodes]))

# extra
labels = {"COM": "CENTER", "YOU": "ME", "SAN": "SAN"}
nx.draw(G, node_size=10, width=0.2, font_color='r', labels=labels, with_labels=True)
plt.show()
