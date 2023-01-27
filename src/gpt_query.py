import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# FINE_TUNED_MODEL = os.getenv('YENACH_GPT_MODEL')
# openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = "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"
# FINE_TUNED_MODEL = "curie:ft-user-2xgdlfxprhvhmrqj32c75xn3-2021-11-10-22-02-38"
FINE_TUNED_MODEL = "curie:ft-user-2xgdlfxprhvhmrqj32c75xn3-2021-11-10-21-32-06"
# Gets a GPT-3 Curie fine-tuned model response to a query
def generate_song():
    open_prompt = ""
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = open_prompt,
        temperature = 1.0,
        max_tokens = 400)
    text = response['choices'][0]['text']
    print(response)
    return text

if __name__ == "__main__":
    print("hello")
    print(generate_song())