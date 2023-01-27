import openai
from graph_generator import text_to_graph
openai.api_key = "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"
# FINE_TUNED_MODEL = "curie:ft-user-2xgdlfxprhvhmrqj32c75xn3-2021-11-10-22-02-38"
FINE_TUNED_MODEL = "text-davinci-003"
# Gets a GPT-3 Curie fine-tuned model response to a query

story = open("../data/stories/story.txt", "r").read()
# k = story.read()
# print(k)
  
# reading the file
def generate_song():
    '''
    Struggling to find an example prompt that will create a consistently formatted output
    Without one, the format may change slightly, but the existence of one will change what
    attributes exist in the output.

    Also need to figure out what counts as an attribute. We will come back to this later after
    the pipeline is complete to see what to optimize. This is just the character + attribute
    angle
    '''
    open_prompt = story + "\n " + "List all characters and their attributes below: \
        \n Example format: \
        \n Albert: good at math, smart"
    print(open_prompt)
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = open_prompt,
        temperature = 0,
        max_tokens = 400)
    text = response['choices'][0]['text']
    print(response)
    # for i in k:

    return text

if __name__ == "__main__":
    print("hello")
    print(generate_song())