import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

similarity_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

"""
Data comes in the form of a graph of chars + relationships
v: Characters + their attributes
e: Character relationships
"""
# Averaged exact-match of the attributes of each character in G1
def compare_graphs_attributes_exact_match(G1, G2):
    similarity = []
    for char in G1.nodes:
        if char in G2.nodes:
            attributes1 = G1.nodes[char]['attributes']
            # handle case where char has no attributes but was in a relationship
            if len(attributes1) == 0:
                continue
            attributes2 = G2.nodes[char]['attributes']
            common_list = set(attributes1).intersection(attributes2)

            total_len = max(len(attributes1), len(attributes2))
            similarity.append(common_list / total_len)
    return sum(similarity) / max(len(G1.nodes), len(G2.nodes))

# Averaged exact-match of the relatinoships of each character-pair in G2
def compare_graphs_relationships_exact_match(G1, G2):
    similarity = []
    for edge in G1.edges:
        if edge in G2.edges:
            relationships1 = G1.edges[edge]['relationships']
            relationships2 = G2.nodes[edge]['relationships']
            common_list = set(relationships1).intersection(relationships2)

            total_len = max(len(relationships1), len(relationships2))
            similarity.append(common_list / total_len)
    return sum(similarity) / max(len(G1.edges), len(G2.edges))

# Averaged semantic similarity of exact matched characters.
# TODO If there is a new character/mismatched character, consider adding penalty
def compare_graphs_attributes_semantic_similarity(G1, G2):
    similarity = []
    G1 = concatenate_graph_attributes(G1)
    G2 = concatenate_graph_attributes(G2)
    for char in G1.keys():
        if char in G2:
            similarity.append(semantic_similarity(G1[char], G2[char]))
    return sum(similarity) / len(similarity)

# Averaged semantic similarity of exact matched character pairs.
# TODO If there is a new character/mismatched relationship, add penalty
def compare_graphs_relationships_semantic_similarity(G1, G2):
    similarity = []
    G1 = concatenate_graph_edges(G1)
    G2 = concatenate_graph_edges(G2)
    for edge in G1.keys():
        if edge in G2:
            similarity.append(semantic_similarity(G1[edge], G2[edge]))
    return sum(similarity) / len(similarity)

# Concatenates char attribute lists to a string for semantic comparison
def concatenate_graph_attributes(G):
    concat_dict = {}
    for i in G.nodes:
        print(G.nodes)
        print(G.nodes[i])
        attributes = G.nodes[i]['attributes']
        concat_dict[i] = ", ".join(attributes)
    return concat_dict

# Concatenates relationship edge lists to a string for semantic comparison
def concatenate_graph_edges(G):
    concat_dict = {}
    for i in G.edges:
        relationships = G.edges[i]['relationships']
        concat_dict[i] = ", ".join(relationships)
    return concat_dict

# Helper function that computes the semantic similarity of two strings
def semantic_similarity(first, second):
    embeddings = similarity_model.encode([first, second])

    first = embeddings[0].reshape(1, -1)
    second = embeddings[1].reshape(1, -1)

    return cosine_similarity(first, second)



if __name__ == "__main__":
    base_G = nx.read_gml("../../data/Character_graphs/basic_story.gml")
    bad_G = nx.read_gml("../data/Character_graphs/bad_scary_story.gml")
    good_G = nx.read_gml("../data/Character_graphs/good_scary_story.gml")
    c_base_G = concatenate_graph(base_G)
    c_bad_G = concatenate_graph(bad_G)
    c_good_G = concatenate_graph(good_G)
    print(compare_concatenated_graphs(c_base_G, c_bad_G))
    print(compare_concatenated_graphs(c_base_G, c_good_G))

