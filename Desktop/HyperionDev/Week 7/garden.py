
import spacy #this is the module we need for NLP

#below is the list for the garden sentences that will be used 
gardenpathsentences = [
    "The complex houses married and single soldiers and their families.",
    "The artistic beauty of the garden is truly amazing.",
    "All the flowers in the garden died for lack of water.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
 ]

import spacy #importing Spcy

nlp = spacy.load('en_core_web_sm') #here the language model that is being used has been loaded after it was downloaded. 

#the following code block will tokenise the model
for sentence in gardenpathsentences: # here, the code is looking over the every sentence that is found in the variable "gardenpathsentences"
    doc = nlp(sentence) #nlp is the pipe that will be used as it has the English model
    named_entities = [(entity.text, entity.label_) for entity in doc.ents] # the categories inside the named entities will be used by the model to categorise the named entities
    print(named_entities) #prints off the entities



