import csv
import networkx as nx

G = nx.Graph()
with open('in.txt') as input_file:
    for row in csv.reader(input_file, delimiter=")"):
        G.add_nodes_from(row)
        G.add_edges_from([row])

print(nx.astar_path_length(G, source='YOU', target='SAN')-2)
