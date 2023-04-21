from graph_generator import generate_character_graph_chat
from gpt_query import gpt_query_chat
from compare_graphs import compare_graphs_attributes_semantic_similarity, compare_graphs_relationships_semantic_similarity
import networkx as nx

# Input: GPT-4 attribute output path
# Returns: Generated graph
def run_graph_construction_from_output(output_path):
    output = open(output_path, "r").read()
    graph = generate_character_graph_chat(output)
    return graph

def run_similarity_from_output(output_path1, output_path2):
    graph1 = run_graph_construction_from_output(output_path1)
    graph2 = run_graph_construction_from_output(output_path2)
    att_sim = compare_graphs_attributes_semantic_similarity(graph1, graph2)
    rel_sim = compare_graphs_relationships_semantic_similarity(graph1, graph2)
    return{
        "att_sim": att_sim,
        "rel_sim": rel_sim
    }

if __name__ == "__main__":
    output_path1 = "../../data/GPT-4_outputs/attributes/test_prompts/test_prompt_good.txt"
    output_path2 = "../../data/GPT-4_outputs/attributes/test_prompts/test_prompt_good2.txt"
    sims = run_similarity_from_output(output_path1, output_path2)
    print(sims["att_sim"])
    print(sims["rel_sim"])
