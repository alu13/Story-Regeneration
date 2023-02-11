import networkx as nx

# viewing character attributes
# print(list(G.nodes))
# print(G.nodes["Albert"])

"""
Text should come in this format

Albert: smart, cool
Anna: dumb, lame

"""
def text_to_graph(text):
    print(text)
    G = nx.Graph()
    # There are 2 newlines at the start
    list_chars = text.split('\n')[2:]
    for i in list_chars:
        # Handle case where line is empty
        if len(i) == 0:
            continue
        char, attributes = i.split(':')
        G.add_node(char, attributes = attributes.split(', '))
    nx.write_gml(G, "good_scary_story.gml")
    return G



# if __name__ == "__main__":
#     # file = open('../data/GPT-3_outputs/Karen.txt', 'r')
#     # text = file.read()
#     # print("hello")
#     # text_to_graph(text)
#     G = nx.read_gml("basic_graph.gml")
#     print(G.nodes)
#     print(G.nodes['Karen'])
