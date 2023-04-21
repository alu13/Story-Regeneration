import openai
openai.api_key = "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"
FINE_TUNED_MODEL = "gpt-4"

'''
Struggling to find an example prompt that will create a consistently formatted output
Without one, the format may change slightly, but the existence of one will change what
attributes exist in the output.

Also need to figure out what counts as an attribute. We will come back to this later after
the pipeline is complete to see what to optimize. This is just the character + attribute
angle

Additional issue with relationships. How do you get GPT to consistently produce direct relationships?
'''

"""
Gets a GPT-3 fine-tuned model response to a query 
Uses the "Completion (simpler) openai endpoint
"""

def gpt_query_completion(story):
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
    return text


"""
Gets a GPT-4 fine-tuned model response to a query 
Uses the "Chat" openai endpoint
"""

def gpt_query_chat(story):
    open_prompt = story + "\n " + "List all main characters and their attributes below. Then list all relationships between characters below that: \
        \n Example format: \
        \n Albert: good at math, smart \
        \n Anna: cool, popular \
        \n (Albert, Anna, friends) \
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
    print("hello")
    story_path = "../../data/stories/ROC_stories/bad_scary_story.txt"
    story = open(story_path, "r").read()
    print(gpt_query_chat(story))