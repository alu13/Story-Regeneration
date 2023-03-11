import openai
openai.api_key = "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"
# from event_graph_generator import text_to_graph
# FINE_TUNED_MODEL = "curie:ft-user-2xgdlfxprhvhmrqj32c75xn3-2021-11-10-22-02-38"
FINE_TUNED_MODEL = "text-davinci-003"
# Gets a GPT-3 Curie fine-tuned model response to a query

# k = story.read()
# print(k)
  
# reading the file
def generate_character_graph(story_file):

    story = open(story_file, "r").read()

    '''
    Struggling to find an example prompt that will create a consistently formatted output
    Without one, the format may change slightly, but the existence of one will change what
    attributes exist in the output.

    Also need to figure out what counts as an attribute. We will come back to this later after
    the pipeline is complete to see what to optimize. This is just the character + attribute
    angle
    '''
    open_prompt = story + "\n " + "List all events that happened in this passage in the format: \
        \n 1. Character, verb, object, modifier \
        \n 2. Character, verb, object, modifier \
        \n 3. Character, verb, object, modifier"
    print(open_prompt)
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = open_prompt,
        temperature = 0,
        max_tokens = 400)
    text = response['choices'][0]['text']
    print(response)
    # G = text_to_graph(text)
    # print(G.nodes)
    # print(G.nodes['Karen'])

    return text

if __name__ == "__main__":
    print("hello")
    story_file = "../../data/stories/writing_prompts/revised_carnival.txt"
    text = generate_character_graph(story_file)
    # text_to_graph(text)
