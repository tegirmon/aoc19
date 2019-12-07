import csv
import networkx as nx

G = nx.DiGraph()
with open('in.txt') as input_file:
    for row in csv.reader(input_file, delimiter=")"):
        G.add_nodes_from(row)
        G.add_edges_from([row])

print(sum([len(nx.ancestors(G, n)) for n in G.nodes]))
