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

def gpt_query_chat(prompt):
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
    print("hello")
    # prompt = "Karen was assigned a roomate her first year of college. Her roomate asked her to go to a nearby city for a concert. Karen agreed happily. The show was absolutely exhilarating.\
    #             \n Rewrite this story but make it scarier. Ensure that \
    #             \n 1. The length of the new story must be similar to the original story \
    #             \n 2. The events must strictly follow this structure:\
    #             \n 3. There must be no new events."
    prompt = "Karen was assigned a roomate her first year of college. Her roomate asked her to go to a nearby city for a concert. Karen agreed happily. The show was absolutely exhilarating.\
                \n Rewrite this story but make it scarier.Ensure that \
                \n 1. The length of the new story must be similar to the original story\
                \n 2. There must be no new events."
    
    print(gpt_query_chat(prompt))