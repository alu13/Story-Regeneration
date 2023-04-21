from .regenerate import gpt_query_chat

def regenerate_passage(story_path, modifier):
    prompt = open(story_path, "r").read()
    return gpt_query_chat(prompt, "scarier")



