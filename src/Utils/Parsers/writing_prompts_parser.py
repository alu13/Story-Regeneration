def replace_newlines(text):
    text = text.replace("<newline> ", "\n")
    return text
if __name__ == "__main__":
    print("hello")
    for i in range(1, 6):
        path = "../../data/stories/writing_prompts/test_stories/prompt" + str(i) + ".txt"
        story = open(path, "r").read()
        text = replace_newlines(story)
        revised_story = open(path, "w")
        revised_story.write(text)
    # text_to_graph(text)