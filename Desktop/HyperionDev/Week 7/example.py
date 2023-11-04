# garden.py

import spacy

gardenpathSentences = [
    "The old man the boats.",
    "The horse raced past the barn fell.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

import spacy

nlp = spacy.load("en_core_web_sm")

# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    named_entities = [(entity.text, entity.label_) for entity in doc.ents]
    print(named_entities)
