from event_graph_generator import text_to_event_list_chat
from gpt_query import gpt_query_chat
from compare_graphs import compare_event_lists_semantic_similarity
import networkx as nx


def test_output_to_similarity(output1_path, output2_path):
    output1 = open(output1_path, "r").read()
    output2 = open(output2_path, "r").read()
    event_list1 = text_to_event_list_chat(output1)
    event_list2 = text_to_event_list_chat(output2)
    return compare_event_lists_semantic_similarity(event_list1, event_list2)

if __name__ == "__main__":
    output1_path = "../../data/GPT-4_outputs/events/test_prompts/test_prompt_base.txt"
    output2_path = "../../data/GPT-4_outputs/events/test_prompts/test_prompt_bad.txt"
    sim = test_output_to_similarity(output1_path, output2_path)
    print(sim)