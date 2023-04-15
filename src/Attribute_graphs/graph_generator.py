import networkx as nx
from itertools import combinations

#TODO: There can be multiple relationships between the same people.

"""
Text should come in this format

Albert: smart, cool
Anna: dumb, lame
(Albert, Anna, friends)
"""
def generate_character_graph_completion(text):
    # There are 2 newlines at the start
    list_chars = text.split('\n')[2:]
    return list_to_graph(text)

"""
There aren't the two initial newlines at the start with the chat endpoint
"""
def generate_character_graph_chat(text):
    # There aren't 2 newlines at the start for chat
    list_chars = text.split('\n')
    return list_to_graph(list_chars)


#Helper function that returns graph G from text list of chars + relationships
def list_to_graph(list_lines):
    G = nx.Graph()
    for line in list_lines:
        # Handle case where line is empty
        if len(line) == 0:
            continue
        if line[0] == "(":
            trio = line[1:-1].split(', ')
            # Handle case where parens has more than 3 elements (extremely uncommon)
            if len(trio) != 3:
                continue
            node1, node2, relationship = trio
            
            # Handle case where one of the people does not have listed attributes
            if (node1 not in G.nodes):
                G.add_node(node1, attributes = [])
            if (node2 not in G.nodes):
                G.add_node(node2, attributes = [])

            if (node1, node2) in G.edges:
                G.edges[(node1, node2)]['relationships'].append(relationship)
            else:
                G.add_edge(node1, node2, relationships = [relationship])
            continue
        char, attributes = line.split(': ')
        G.add_node(char, attributes = attributes.split(', '))
    G = cleanup_graph(G)
    return G

# Merge nodes thats are similar (and likely the same character)
# This uses overlap similarity because semantic similarity would be too compute-intensive. O(n^2) model calls
def cleanup_graph(G):
    for i, j in combinations(G.nodes(), 2):
        # Handle case where a node got deleted
        if i not in G:
            continue
        if (i.lower() in j.lower()) or (j.lower() in i.lower()):
            G.nodes[i]["attributes"] += G.nodes[j]["attributes"]

            # replace edges
            for neighbor in G.neighbors(j):
                if neighbor not in G.neighbors(i):
                    G.add_edge(i, neighbor, relationships = G.edges[j, neighbor]["relationships"])
                else:
                    G.edges[i, neighbor]["relationships"] += G.edges[j, neighbor]["relationships"]
            G.remove_node(j)
    return G

if __name__ == "__main__":
    file = open('../../data/GPT-4_outputs/attributes/bad_scary_story.txt', 'r')
    text = file.read()
    G = generate_character_graph_chat(text)
    for i in G.nodes:
        print(i)
        print(G.nodes[i]['attributes'])
    for e in G.edges:
        print(e)
        print(G.edges[e]['relationships'])
    # nx.write_gml(G, "bad_scary_story.gml")
    # G = nx.read_gml("base_scary_story.gml")
    # print(G.nodes)
    # print(G.nodes['Karen'])
    # print(G.edges[('Karen', 'Roommate')])
