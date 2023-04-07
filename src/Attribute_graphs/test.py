import networkx as nx
G = nx.Graph()

G.add_edge(1, 2, relationship = ["hello"])
G.edges[(1, 2)]["relationship"].append("no")
print(G.edges[(1, 2)]["relationship"])

print(G.edges)