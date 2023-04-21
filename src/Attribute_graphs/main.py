from .graph_generator import generate_character_graph_chat
from .gpt_query import gpt_query_chat
from .compare_graphs import compare_graphs_attributes_semantic_similarity, compare_graphs_relationships_semantic_similarity
import networkx as nx


# Input: two graph paths
# The purpose of inputting graphs is to remove the variability of GPT-4 and test on fixed data
# Returns: Attribute similarity
def run_attribute_similarity(graph1_path, graph2_path, comparison_type="hard"):
    graph1 = nx.read_gml(graph1_path)
    graph2 = nx.read_gml(graph2_path)
    return compare_graphs_attributes_semantic_similarity(graph1, graph2, comparison_type)

# Input: two graph paths
# Returns: relationship similarity
def run_relationship_similarity(graph1_path, graph2_path, comparison_type="hard"):
    graph1 = nx.read_gml(graph1_path)
    graph2 = nx.read_gml(graph2_path)
    return compare_graphs_relationships_semantic_similarity(graph1, graph2, comparison_type)

# Input: story path
# Returns: Generated graph
def run_graph_construction(story_path):
    story = open(story_path, "r").read()
    text_response = gpt_query_chat(story)
    graph = generate_character_graph_chat(text_response)
    return graph

# Input: two story paths
# Returns: attribute/relationship similarity of these two stories
def run_entire_process(story_path1, story_path2, comparison_type="hard"):
    char_graph1 = run_graph_construction(story_path1)
    char_graph2 = run_graph_construction(story_path2)
    attribute_sim = compare_graphs_attributes_semantic_similarity(char_graph1, char_graph2, comparison_type)
    relationship_sim = compare_graphs_relationships_semantic_similarity(char_graph1, char_graph2, comparison_type)
    return {
        "attribute_similarity": attribute_sim,
        "relationship_similarity": relationship_sim
    }

# Print all nodes, edges, and node/edge attributes
def print_graph(graph):
    for i in graph.nodes:
        print(i)
        print(graph.nodes[i])
    for i in graph.edges:
        print(i)
        print(graph.edges[i])

if __name__ == "__main__":
    story_1_path = "../../data/Character_graphs/GPT-4/test_prompts/test_prompt_base.gml"
    story_2_path = "../../data/Character_graphs/GPT-4/test_prompts/test_prompt_good.gml"
    sim = run_relationship_similarity(story_1_path, story_2_path, comparison_type = "overlap")
    print(sim)
    # g1 = run_graph_construction_from_output(story_1_path)
    # print_graph(g1)
    # nx.write_gml(g1, 'test_prompt_base.gml')

    # g2 = run_graph_construction_from_output(story_2_path)
    # print_graph(g2)
    # nx.write_gml(g2, 'test_prompt_good.gml')
    # similarity = run_entire_process(story_1_path, story_2_path)
    # print(similarity)
    # graph_1_path = "../../data/Character_graphs/GPT-4/base_story.gml"
    # graph_2_path = "../../data/Character_graphs/GPT-4/bad_scary_story.gml"
    # similarity = run_relationship_similarity(graph_1_path, graph_2_path)
    # print(similarity)