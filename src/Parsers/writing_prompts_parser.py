def replace_newlines(text):
    text = text.replace("<newline> ", "\n")
    return text
if __name__ == "__main__":
    print("hello")
    story_file = "../../data/stories/writing_prompts/carnival.txt"
    story = open(story_file, "r").read()
    text = replace_newlines(story)
    new_story_file = "../../data/stories/writing_prompts/revised_carnival.txt"
    revised_story = open(new_story_file, "x")
    revised_story.write(text)
    # text_to_graph(text)