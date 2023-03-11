import spacy
import coreferee

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('coreferee')

def coreference_transform(text):
    coref_doc = nlp(text)

    resolved_text = ""
    print(coref_doc._.coref_chains)
    #Token by token check if there is a head, and if so take it.
    for token in coref_doc:
        repres = coref_doc._.coref_chains.resolve(token)
        if repres:
            resolved_text += " " + " and ".join([t.text for t in repres])
        else:
            resolved_text += " " + token.text
    return resolved_text
    
if __name__ == "__main__":
    test = coreference_transform("My name is Albert Lu. I have a friend named Teddy. He is going to the store today.")
    print(test)
