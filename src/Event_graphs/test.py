import networkx as nx

G = nx.Graph()
dic = {
    "verb": "hello",
    "order": 2
}
G.add_edge(1, 3, 
           verb = "hello",
           order = 2)
for i in G.edges:
    print(G.edges[i])