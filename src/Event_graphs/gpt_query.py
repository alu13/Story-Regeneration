import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
FINE_TUNED_MODEL = "gpt-4"

# Gets a GPT-3 Curie fine-tuned model response to a query
def gpt_query_completion(story):

    open_prompt = story + "\n " + "List all events that happened in this passage in the format: \
        \n 1. Character, verb, object, modifier \
        \n 2. Character, verb, object, modifier \
        \n 3. Character, verb, object, modifier"
    # print(open_prompt)
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = open_prompt,
        temperature = 0,
        max_tokens = 400)
    text = response['choices'][0]['message']['content']
    print(text)
    return text

def gpt_query_chat(story):

    open_prompt = story + "\n " + "List all high-level events that happened in this passage in the format: \
        \n 1. Character, verb, object, modifier \
        \n 2. Character, verb, object, modifier \
        \n 3. Character, verb, object, modifier \
        \n If there is a character 'I', refer to them as Protagonist"
    print(open_prompt)
    response = openai.ChatCompletion.create(
        model = FINE_TUNED_MODEL,
        messages = [
            {"role": "user", "content": open_prompt}
        ],
        temperature = 0,
        max_tokens = 400)
    text = response['choices'][0]['message']['content']
    print(text)
    return text


if __name__ == "__main__":
    story_file = "../../data/stories/ROC_stories/story.txt"
    text = gpt_query_chat(story_file)
    # text_to_graph(text)
