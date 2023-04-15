from Attribute_graphs.main import run_entire_process as attribute_similarity
from Event_graphs.main import run_entire_process as event_similarity

def run_similarity_computation(story1_path, story2_path):
    char_sim = attribute_similarity(story1_path, story2_path)
    attribute_sim = char_sim["attribute_similarity"]
    relationship_sim = char_sim["relationship_similarity"]
    event_sim = event_similarity(story1_path, story2_path)
    print("attribute_sim" + str(attribute_sim))
    print("relationship_sim" + str(relationship_sim))
    print("sum = " + str(attribute_sim + relationship_sim))
    print("event_sim" + str(event_sim))
    average_sim = (attribute_sim + relationship_sim) / 4 + (event_sim) / 2
    return {
        "attribute_sim": attribute_sim,
        "relationship_sim": relationship_sim,
        "event_sim": event_sim,
        "average_sim": average_sim
    }

if __name__ == "__main__":
    story1_path = "../data/stories/ROC_stories/story.txt"
    story2_path = "../data/stories/ROC_stories/bad_scary_story.txt"
    sims = run_similarity_computation(story1_path, story2_path)
    attribute_sim = sims["attribute_sim"]
    relationship_sim = sims["relationship_sim"]
    event_sim = sims["event_sim"]
    average_sim = sims["average_sim"]
    print("attribute sim: " + str(attribute_sim))
    print("relationship sim: " + str(relationship_sim))
    print("event sim: " + str(event_sim))
    print("averaged sim = " + str(average_sim))
