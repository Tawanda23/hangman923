
cool_sentence = "My very enerst mother just served us nuts please"

modified_sentence = ""

for i in range(len(cool_sentence)):

    if i % 2 == 1:

        modified_sentence += cool_sentence[i].lower()

    else:
        modified_sentence += cool_sentence[i].upper()

print(modified_sentence)



#Part 2 

# this asks the user to type in a cool sentence
cool_statement = input("Please type a sentence: \n  ") 

# this splits the sentence string that the user will have input
sentence = cool_statement.split() 

# this is the variable that will be used to store the new string
alternative_word = [] 

for i in range(len(sentence)):

# here, the loop checks if the index we have  is odd or even, if its even, 
    if i % 2 == 0: #checks if the word is odd or is even

#this changes the word to match the new word on the even string
        alternative_word.append(sentence[i].lower()) 
    else:
        alternative_word.append(sentence[i].upper())

#line to create modified sentence by joining lower and upper cases
modified_sentence = " ".join(alternative_word) 

print(modified_sentence)
