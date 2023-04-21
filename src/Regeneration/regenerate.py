import openai
openai.api_key = "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"
FINE_TUNED_MODEL = "gpt-4"

"""
Gets a GPT-4 fine-tuned model response to a query 
Uses the "Chat" openai endpoint
"""

def gpt_query_chat(prompt, modifier):
    prompt += "\n Rewrite this story but make it " + str(modifier) + ". Ensure that \
                \n 1. The length of the new story must be similar to the original story\
                \n 2. There must be no new events."
    response = openai.ChatCompletion.create(
        model = FINE_TUNED_MODEL,
        messages = [
            {"role": "user", "content": prompt}
        ],
        temperature = 0.7,
        max_tokens = 1024)
    text = response['choices'][0]['message']['content']
    return text

def gpt_query_chat_bad(prompt, modifier):
    prompt += "\n Rewrite this story but make it " + str(modifier) + ". Additionally, make sure to change the plot completely."

    response = openai.ChatCompletion.create(
        model = FINE_TUNED_MODEL,
        messages = [
            {"role": "user", "content": prompt}
        ],
        temperature = 0.7,
        max_tokens = 1024)
    text = response['choices'][0]['message']['content']
    return text
if __name__ == "__main__":
    story_1_path = "../../data/stories/writing_prompts/test_stories/prompt5_materials/prompt5.txt"
    prompt = open(story_1_path, "r").read()
    print(gpt_query_chat_bad(prompt, "more optimistic"))