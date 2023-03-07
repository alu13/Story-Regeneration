import networkx as nx

# viewing character attributes
# print(list(G.nodes))
# print(G.nodes["Albert"])

"""
Text should come in this format 1. <s, v, o, m>

1. Albert, went, to the market, quickly
2. Anna, bought, corgi, from the store

"""
def text_to_event_list(text):
    print(text)
    G = nx.Graph()
    # There are 2 newlines at the start
    list_chars = text.split('\n')[2:]
    events = []
    for i in list_chars:
        # Handle case where line is empty
        if len(i) == 0:
            continue

        # Bypass numbered section of the list
        event_rep = i[3:].split(', ')
        if len(event_rep) > 4:
            event_rep = event_rep[:4]

        # Replace modifier/DO with empty strings if they don't exist
        filler = [''] * (4 - len(event_rep))
        event_rep += filler
        events.append({
            "subject": event_rep[0], 
            "verb": event_rep[1], 
            "object": event_rep[2], 
            "modifier": event_rep[3]
        })

        # Considering reader model construction
        # G.add_node(char, subject = event_rep[0], 
        #            verb = event_rep[1], 
        #            object = event_rep[2], 
        #            modifier = event_rep[3])
    print(events)
    return events

"""
Plan:

Text should come in this format 1. <s, v, o, m>

Consider removing modifier for noise reasons.
Consider using similarity checker to match ndoes to each other
"her roomate" vs "the roomate" should be the same (?)

1. Albert, went, to the market, quickly
2. Anna, bought, corgi, from the store

Construct labeled graph (s, o) edges, (v) vertices
temporal component (in vertice) for when action happens. 
"""

def text_to_event_graph(text):
    G = nx.Graph()
    # There are 2 newlines at the start
    list_chars = text.split('\n')[2:]
    events = []
    event_num = 0
    for i in list_chars:
        # Handle case where line is empty
        if len(i) == 0:
            continue

        # Bypass numbered section of the list
        event_rep = i[3:].split(', ')

        # Cap values at <s, v, o, m>
        if len(event_rep) > 4:
            event_rep = event_rep[:4]

        # Replace modifier/DO with empty strings if they don't exist
        filler = [''] * (4 - len(event_rep))
        event_rep += filler

        subject, verb, object, modifier = event_rep
        G.add_edge(subject, object, verb = verb, order = event_num)

        event_num += 1

    nx.write_gml(G, "good_scary_story.gml")
    return G




if __name__ == "__main__":
    file = open('../../data/GPT-3_outputs/events/Karen.txt', 'r')
    text = file.read()
    # print("hello")
    G = text_to_event_graph(text)
    print(G.nodes)
    for i in G.edges:
        print(G.edges[i])
