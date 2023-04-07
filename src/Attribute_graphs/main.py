from graph_generator import generate_character_graph_chat
from gpt_query import gpt_query_chat
from compare_graphs import compare_graphs_attributes_semantic_similarity
import networkx as nx

def run_graph_similarity(graph1_path, graph2_path):
    graph1 = nx.read_gml(graph1_path)
    graph2 = nx.read_gml(graph1_path)
    return compare_graphs_attributes_semantic_similarity(graph1, graph2)

def run_graph_construction(story_path):
    story = open(story_path, "r").read()
    text_response = gpt_query_chat(story)
    graph = generate_character_graph_chat(text_response)
    return graph


def run_entire_process(story_path1, story_path2):
    char_graph1 = run_graph_construction(story_path1)
    char_graph2 = run_graph_construction(story_path2)
    return compare_graphs_attributes_semantic_similarity(char_graph1, char_graph2)

if __name__ == "__main__":
    story_1_path = "../../data/stories/ROC_stories/story.txt"
    story_2_path = "../../data/stories/ROC_stories/good_scary_story.txt"

    similarity = run_entire_process(story_1_path, story_2_path)
    print(similarity)