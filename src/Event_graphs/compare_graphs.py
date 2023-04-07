import networkx as nx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

similarity_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

"""
Input: two lists of event dictionaries
Attributes: subject, verb, object, modifier

Output: Averaged exact match similarity of <s, v, o, m> of events in both lists.
"""
def compare_event_lists_exact_match(l1, l2):
    # Averaged exact match similarity of <s, v, o, m> of events in both lists.
    # Takes the maximum
    similarity = []
    for i in range(len(l1)):
        max_similarity = 0
        for j in range(len(l2)):
            event1 = l1[i]
            event2 = l2[j]
            curr_similarity = 0

            # 4 keys (s, v, o, m)
            for key in event1.keys():
                if event1[key] == event2[key]:
                    curr_comp += 0.25

            # Scale by difference in event numbers.
            # Equal events should not be far apart (timewise)

            total_len = max(len(l1), len(l2))
            scaling_factor = (total_len - abs(i - j)) / total_len

            if curr_similarity * scaling_factor >= max_similarity:
                max_similarity = curr_similarity

    similarity.append(max_similarity)
    return sum(similarity) / len(similarity)

"""
Input: two lists of event dictionaries
Attributes: subject, verb, object, modifier

Output: Averaged semantic similarity of strings "s, v, o, m" of events in both lists.
"""
def compare_event_lists_semantic_similarity(l1, l2):
    print(l1)
    print(l2)
    similarity = []
    for i in range(len(l1)):
        max_similarity = 0
        for j in range(len(l2)):
            vals1 = [l1[i].get(k) for k in ["subject", "verb", "object", "modifier"]]
            vals2 = [l2[j].get(k) for k in ["subject", "verb", "object", "modifier"]]
            event1 = ', '.join(vals1)
            event2 = ', '.join(vals2)
            curr_similarity = semantic_similarity(event1, event2)
            print("event1 = " + str(event1))
            print("event2 = " + str(event2))
            print("similarity = " + str(curr_similarity))
            # Scale by difference in event numbers.
            # Equal events should not be far apart (timewise)

            total_len = max(len(l1), len(l2))
            scaling_factor = (total_len - abs(i - j)) / total_len

            if curr_similarity * scaling_factor >= max_similarity:
                max_similarity = curr_similarity

    similarity.append(max_similarity)
    return sum(similarity) / len(similarity)

# Computes the semantic similarity of two sentences
# Takes model embeddings of phrases and computes their cosine similarities
def semantic_similarity(phrase1, phrase2):

    embeddings = similarity_model.encode([phrase1, phrase2])

    first = embeddings[0].reshape(1, -1)
    second = embeddings[1].reshape(1, -1)

    return(cosine_similarity(first, second))

if __name__ == "__main__":
    base_G = nx.read_gml("../data/Character_graphs/basic_story.gml")
    bad_G = nx.read_gml("../data/Character_graphs/bad_scary_story.gml")
    good_G = nx.read_gml("../data/Character_graphs/good_scary_story.gml")

