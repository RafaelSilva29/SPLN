from re import sub, findall
import fileinput
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

import shelve

with shelve.open("HarryPotterRelations_DB") as hp:
    print(list(hp.items()))

    G = nx.Graph()
    for x in list(hp.items()):
        G.add_edge(x[1]["Name"], x[1]["Friend Name"])

    plt.figure(figsize = (15, 15))
    nx.draw(G, with_labels = True, node_size = 1500, font_size = 10)
    plt.show()