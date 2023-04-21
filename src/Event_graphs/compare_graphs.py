import networkx as nx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.optimize import linear_sum_assignment

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
    for i in range(len(l1)):
        l1[i] = ', '.join([l1[i].get(k) for k in ["subject", "verb", "object", "modifier"]])
    for i in range(len(l2)):
        l2[i] = ', '.join([l2[i].get(k) for k in ["subject", "verb", "object", "modifier"]])
    # Uncomment to see the two event lists you can comparing
    for i in l1:
        print(i)
    print("\n")
    for i in l2:
        print(i)
    # Purpose of the max is to create cols of 0s if the list_of_events l2 is too short
    similarity = np.zeros((len(l1), max(len(l2), len(l1))))
    for i in range(len(l1)):
        for j in range(len(l2)):
            curr_similarity = semantic_similarity(l1[i], l2[j])

            # Scale by difference in event numbers.
            # Equal events should not be far apart (timewise)
            total_len = max(len(l1), len(l2))
            scaling_factor = (total_len - abs(i - j)) / total_len
            similarity[i, j] = curr_similarity * scaling_factor

    max_similarity = np.sum(np.amax(similarity, axis=1)) / len(l1)

    # Performs maximal matching on a matrix of SS scorings between all events
    # Ideally, events are 1-to-1, but that's often not the case, so deprecating.
    # Still used for penalty term though.
    rows, cols = linear_sum_assignment(similarity, maximize = True)
    # matched_similarity = similarity[rows, cols].sum() / len(l1)

    # Penalize if story 2 has TOO MANY EVENTS
    extra_events = [i for i in range(len(l2)) if i not in cols]
    print("extra_events" + str(extra_events))
    # Closeness is a measure of how similar these extra events are to the original story
    # i.e. if there is overlap between the orignial story and these events, then less penalty
    closeness = np.sum(np.amax(similarity[:, extra_events], axis=0))
    print("closeness" + str(closeness))

    # 1 if story1 has more events than story2
    event_penalty = min((len(l1) + closeness) / len(l2), 1)
    print("event penalty: " + str(event_penalty))
    print("max similarity: " + str(max_similarity))
    return max_similarity * event_penalty

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

