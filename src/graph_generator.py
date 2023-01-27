import networkx as nx
G = nx.Graph()


# Adding chars and attributes to graphs
G.add_node("Albert", attributes = ["smart", "cool"])
G.add_node("Anna", attributes = ["lame", "dumb"])

# viewing character attributes
print(list(G.nodes))
print(G.nodes["Albert"])

"""
Text should come in this format

Albert: smart, cool
Anna: dumb, lame

"""
file = open('../data/GPT-3_outputs/Karen.txt', 'r')
text = file.read()
def text_to_graph(text):
    # There are 2 newlines at the start
    list_chars = text.split('\n')[2:]
    for i in list_chars:
        char, attributes = i.split(':')
        print(char)
        print(attributes)