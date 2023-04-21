import openai
openai.api_key = "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"
FINE_TUNED_MODEL = "gpt-4"

def gpt4_baseline_similarity(story1, story2):

    open_prompt =  "Story 1: \n" + str(story1) + "\n Story2: \n" \
        + str(story2) + "\n\n Rate the similarity of these two stories on a scale of 0-1:"
    # print(open_prompt)
    response = openai.ChatCompletion.create(
        model = FINE_TUNED_MODEL,
        messages = [
            {"role": "user", "content": open_prompt}
        ],
        temperature = 0.7,
        max_tokens = 400)
    text = response['choices'][0]['message']['content']
    print(text)
    return text

# def gpt4_summary_baseline_similarity(story1, story2):
