import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

similarity_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def concatenate_graph(G):
    concat_dict = {}
    for i in G.nodes:
        attributes = G.nodes[i]['attributes']
        concat_dict[i] = ", ".join(attributes)
    return concat_dict

def compare_concatenated_graphs(G1, G2):
    # Averaged semantic similarity of exact matched characters.
    # If there is a new character/mismatched character, add penalty
    similarity = []
    for char in G1.keys():
        if char in G2:
            similarity.append = semantic_similarty(G1['char'], G2['char'])
    return sum(similarity) / len(similarity)

def semantic_similarty(first, second):
    embeddings = similarity_model.encode([first, second])

    first = embeddings[0].reshape(1, -1)
    second = embeddings[1].reshape(1, -1)

    return cosine_similarity(first, second)



if __name__ == "__main__":
    base_G = nx.read_gml("../data/Character_graphs/basic_story.gml")
    bad_G = nx.read_gml("../data/Character_graphs/bad_scary_story.gml")
    good_G = nx.read_gml("../data/Character_graphs/good_scary_story.gml")
    c_base_G = concatenate_graph(base_G)
    c_bad_G = concatenate_graph(bad_G)

