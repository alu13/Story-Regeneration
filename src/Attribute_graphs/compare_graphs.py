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
    print(G1.nodes)
    print(G2.nodes)
    similarity = []
    for char in G1.nodes:
        if char in G2.nodes:
            attributes1 = G1.nodes[char]['attributes']
            # handle case where char has no attributes but was in a relationship
            if len(attributes1) == 0:
                continue
            attributes2 = G2.nodes[char]['attributes']
            print(attributes1)
            print(attributes2)
            common_list = set(attributes1).intersection(attributes2)

            total_len = max(len(attributes1), len(attributes2))
            similarity.append(len(common_list) / total_len)
    return sum(similarity) / max(len(G1.nodes), len(G2.nodes))

# Averaged exact-match of the relationships of each character-pair in G2
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

# Averaged semantic similarity of matched characters.
# Hard : Characters must exactly match
# Overlap: One char must be a substring of another (roommate, college roommate)
# Soft: Characters must have a high semantic similarity (i.e 0.7)
# TODO If there is a new character/mismatched character, consider adding penalty
def compare_graphs_attributes_semantic_similarity(G1, G2, comparison_type = "hard"):
    similarity = []
    G1 = concatenate_graph_attributes(G1)
    G2 = concatenate_graph_attributes(G2)
    bar = 0.7
    if comparison_type == "hard":
        for char in G1.keys():
            if char in G2.keys():
                similarity.append(semantic_similarity(G1[char], G2[char]))
    elif comparison_type == "overlap":
        for char1 in G1.keys():
            for char2 in G2.keys():
                if overlap_compare_chars(char1, char2):
                    similarity.append(semantic_similarity(G1[char1], G2[char2]))
                    break
    elif comparison_type == "soft":
        for char1 in G1.keys():
            for char2 in G2.keys():
                if soft_compare_rels(char1, char2, bar):
                    similarity.append(semantic_similarity(G1[char1], G2[char2]))
                    break
    #Handle case for no matching characters
    if len(similarity) == 0:
        return 0
    return sum(similarity) / len(similarity)

# Averaged semantic similarity of exact matched character pairs.
# Hard : Characters must exactly match
# Overlap: One char must be a substring of another (roommate, college roommate)
# Soft: Characters must have a high semantic similarity (i.e 0.7)
# TODO If there is a new character/mismatched relationship, add penalty
def compare_graphs_relationships_semantic_similarity(G1, G2, comparison_type = "hard"):
    similarity = []
    G1 = concatenate_graph_edges(G1)
    G2 = concatenate_graph_edges(G2)
    print("G1:" + str(G1))
    print("G2:" + str(G2))
    bar = 0.7
    if comparison_type == "hard":
        for rel in G1.keys():
            if rel in G2.keys():
                similarity.append(semantic_similarity(G1[rel], G2[rel]))
    elif comparison_type == "overlap":
        for rel1 in G1.keys():
            for rel2 in G2.keys():
                if overlap_compare_rels(rel1, rel2):
                    similarity.append(semantic_similarity(G1[rel1], G2[rel2]))
                    break
    elif comparison_type == "soft":
        for rel1 in G1.keys():
            for rel2 in G2.keys():
                if soft_compare_rels(rel1, rel2, bar):
                    similarity.append(semantic_similarity(G1[rel1], G2[rel2]))
                    break

    #Handle case for no matching character pairs
    if len(similarity) == 0:
        return 0
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

# Check if two characters overlap (should be considered the same)
def overlap_compare_chars(char1, char2):
    if (char1.lower() in char2.lower()) or (char2.lower() in char1.lower()):
        return True
    return False
# Check if two charactesr are semantically similar
def soft_compare_chars(char1, char2, bar):
    if semantic_similarity(char1, char2) > bar:
        return True
    return False

# Check if two relationships have similar characters (by overlap)
def overlap_compare_rels(rel1, rel2):
    # case where (1, 0) = (1, 0)
    if ((rel1[0].lower() in rel2[0].lower()) or (rel2[0].lower() in rel1[0].lower()) and
        (rel1[1].lower() in rel2[1].lower()) or (rel2[1].lower() in rel1[1].lower())):
        print("in here")
        return True
    
    # case where (0, 1) == (1, 0) 
    # rel edges are bidirectional so we have to check both
    elif ((rel1[1].lower() in rel2[0].lower()) or (rel2[0].lower() in rel1[1].lower()) and
        (rel1[0].lower() in rel2[1].lower()) or (rel2[1].lower() in rel1[0].lower())):
        print("here instead")
        return True
    print("return false")
    return False

# Check if two relationships are semantically similar
# Requires 4 similarity checks. Might be too expensive.
def soft_compare_rels(rel1, rel2, bar):
    # case where (1, 0) = (1, 0)
    if ((semantic_similarity(rel1[0], rel2[0]) > bar) and (semantic_similarity(rel1[1], rel2[1]) > bar)):
        return True
    
    # case where (0, 1) == (1, 0) 
    # rel edges are bidirectional so we have to check both
    elif ((semantic_similarity(rel1[1], rel2[0]) > bar) and (semantic_similarity(rel1[0], rel2[1]) > bar)):
        return True
    return False

# Helper function that computes the semantic similarity of two strings
def semantic_similarity(first, second):
    embeddings = similarity_model.encode([first, second])

    first = embeddings[0].reshape(1, -1)
    second = embeddings[1].reshape(1, -1)

    return cosine_similarity(first, second)

if __name__ == "__main__":
    base_G = nx.read_gml("../../data/Character_graphs/GPT-4/base_story.gml")
    bad_G = nx.read_gml("../../data/Character_graphs/GPT-4/bad_scary_story.gml")
    good_G = nx.read_gml("../../data/Character_graphs/GPT-4/good_scary_story.gml")
    # c_base_G = concatenate_graph(base_G)
    # c_bad_G = concatenate_graph(bad_G)
    # c_good_G = concatenate_graph(good_G)
    # print(compare_concatenated_graphs(c_base_G, c_bad_G))
    # print(compare_concatenated_graphs(c_base_G, c_good_G))
    sim = compare_graphs_relationships_semantic_similarity(base_G, good_G, "hard")
    print(sim)
    # print(sim)
    # print(concatenate_graph_edges(base_G))

