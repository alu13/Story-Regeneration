from event_graph_generator import text_to_event_list_chat
from gpt_query import gpt_query_chat
from compare_graphs import compare_event_lists_semantic_similarity
import networkx as nx

def run_list_similarity(list1_path, list2_path):
    list1 = open(list1_path, "r").read()
    list2 = open(list2_path, "r").read()
    event_list1 = text_to_event_list_chat(list1)
    event_list2 = text_to_event_list_chat(list2)
    print(event_list1)
    return compare_event_lists_semantic_similarity(event_list1, event_list2)

def run_list_construction(story_path):
    story = open(story_path, "r").read()
    text_response = gpt_query_chat(story)
    event_list = text_to_event_list_chat(text_response)
    return event_list


def run_entire_process(story_path1, story_path2):
    char_list1 = run_list_construction(story_path1)
    char_list2 = run_list_construction(story_path2)
    return compare_event_lists_semantic_similarity(char_list1, char_list2)

if __name__ == "__main__":
    story_1_path = "../../data/stories/ROC_stories/story.txt"
    story_2_path = "../../data/stories/ROC_stories/good_scary_story.txt"

    # similarity = run_entire_process(story_1_path, story_2_path)
    # print(similarity)
    list1_path = "../../data/GPT-4_outputs/events/base_story.txt"
    list2_path = "../../data/GPT-4_outputs/events/good_scary_story.txt"
    similarity = run_list_similarity(list1_path, list2_path)
    print(similarity)