from Event_graphs.graph_generator import text_to_graph, generate_character_graph
from gpt_query import gpt_query
from compare_graphs import compare_attribute_lists

def run_graph_similarity(graph1_path, graph2_path):
    graph1 = get_graph(graph1_path)
    graph2 = get_graph(graph1_path)
    return compare_attribute_graphs(graph1, graph2)

def run_graph_construction(story_path):
    story = open(story_path, "r").read()
    text_response = gpt_query(story)
    graph = generate_character_graph(text_response)
    return graph


def run_entire_process(story_path1, story_path2):
    char_graph1 = run_graph_construction(story_path1)
    char_graph2 = run_graph_construction(story_path2)
    return compare_attribute_graphs(char_graph1, char_graph2)

# Put in gpt_query file
def query_gpt()
