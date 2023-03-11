import networkx as nx

"""
Input: two lists of event dictionaries
Attributes: subject, verb, object, modifier

Output: Averaged exact match similarity of <s, v, o, m> of events in both lists.
"""
def compare_event_lists(l1, l2):
    # Averaged exact match similarity of <s, v, o, m> of events in both lists.
    # Takes the maximum
    similarity = []
    for i in range(len(l1)):
        max_similarity = 0
        for j in range(len(l2)):
            event1 = l1[i]
            event2 = l2[j]
            curr_similarity = 0

            for key in event1.keys():
                if event1[key] == event2[key]:
                    curr_comp += 0.25

            # Scale by difference in event numbers.
            # Equal events should not be far apart (timewise)

            total_len = max(i, j)
            scaling_factor = (total_len - abs(i - j)) / total_len

            if curr_similarity * scaling_factor >= max_similarity:
                max_similarity = curr_similarity

    similarity.append(max_similarity)
    return sum(similarity) / len(similarity)

if __name__ == "__main__":
    base_G = nx.read_gml("../data/Character_graphs/basic_story.gml")
    bad_G = nx.read_gml("../data/Character_graphs/bad_scary_story.gml")
    good_G = nx.read_gml("../data/Character_graphs/good_scary_story.gml")
    c_base_G = concatenate_graph(base_G)
    c_bad_G = concatenate_graph(bad_G)

