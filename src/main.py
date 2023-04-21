import tempfile
import pandas as pd

from Attribute_graphs.main import run_entire_process as attribute_similarity
from Event_graphs.main import run_entire_process as event_similarity
from Regeneration.main import regenerate_passage
from Utils.semantic_similarity import semantic_similarity as ss_baseline
from Utils.gpt4_baseline import gpt4_baseline_similarity as gpt4_baseline

# Takes in two story paths and returns our similarity metric
def run_similarity_computation(story1_path, story2_path, comparison_type="hard"):
    char_sim = attribute_similarity(story1_path, story2_path, comparison_type)
    attribute_sim = char_sim["attribute_similarity"]
    relationship_sim = char_sim["relationship_similarity"]
    event_sim = event_similarity(story1_path, story2_path)
    # average_sim = (attribute_sim + relationship_sim) / 4 + (event_sim) / 2
    average_sim = (attribute_sim) / 4 + (event_sim) * (3/4)

    print("attribute_sim" + str(attribute_sim))
    print("relationship_sim" + str(relationship_sim))
    print("sum = " + str(attribute_sim + relationship_sim))
    print("event_sim" + str(event_sim))
    print("average_sim = " + str(average_sim))

    return {
        "attribute_sim": attribute_sim,
        "relationship_sim": relationship_sim,
        "event_sim": event_sim,
        "average_sim": average_sim
    }

# Takes in a story path + modifiers and returns a list of GPT-3 story generations
# Stories are ranked by our score metric.
def stories_ranked(story_path, story_name, modifier, num_outputs):
    stories = []
    for i in range(num_outputs):
        new_story = regenerate_passage(story_path, modifier)
        
        # Because the similarity computation takes files, create a tempfile for the new story
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            # Write your string to the file
            f.write(new_story)

            # Get the filename of the temporary file
            new_story_path = f.name
        similarity = run_similarity_computation(story_path, new_story_path)
        stories.append({
            "Story": new_story,
            "similarity_score": similarity['average_sim']
        })
    df = pd.DataFrame(stories)
    df = df.sort_values("similarity_score", ascending=False)
    df.to_csv(story_name + ".csv", index=False)

# Takes in two story paths and returns their similarity
def story_similarity_baselines(story1_path, story2_path, comparison_type="hard"):
    story1 = open(story1_path, "r").read()
    story2 = open(story2_path, "r").read()

    test_sim = run_similarity_computation(story1_path, story2_path, "overlap")["average_sim"]
    ss = ss_baseline(story1, story2)
    gpt4 = gpt4_baseline(story1, story2)

    return {
        "test_sim":test_sim,
        "ss_baseline": ss,
        "gpt4_baseline": gpt4
    }

if __name__ == "__main__":
    # story1_path = "../data/stories/ROC_stories/test_stories/prompt1.txt"
    # stories_ranked(story1_path, "roc_story_1", "more suspenseful", 3)
    story1_path = "../data/stories/writing_prompts/test_stories/prompt4_materials/prompt4.txt"
    story2_path = "../data/stories/writing_prompts/test_stories/prompt4_materials/prompt4_bad.txt"
    story_sim = story_similarity_baselines(story1_path, story2_path, "overlap")
    print(story_sim)