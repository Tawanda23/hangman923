import spacy #this is the module we need for NLP

nlp = spacy.load('en_core_web_sm')

sample = "The quick brown fox, jumps over the lazy dog."

doc = nlp(sample)

print([token.orth_ for token in doc]) #how spacy see the sentence

for word in doc: # words that sapce thinks are stop words
    if word.is_stop == True:
        print(word)

#lamatisation gives the origin word

sample = "sing sang singing"
doc = nlp(sample)

print([token.lemma_ for token in doc])

#Entity Recognition 

wiki_priyanka = "known by her married name Priyanka Chopra Jonas, is an Indian actress, singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.One of India's highest-paid and most popular celebrities, Chopra has received numerousawards, including a National Film Award and five Filmfare Awards. In 2016, the Governmentof India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."

nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label) for i in nlp_priyanka.ents])

entity_fac = spacy.explain("NORP") #this stores what the explanation of the category is 
print(f"FAC:{entity_fac}")