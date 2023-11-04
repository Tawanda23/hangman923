#New file called replace.py

#replaces ! 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
print(sentence.replace("!", " "))

#This changes the caps of the string into upper caps and then replaces !
sentence2 = (sentence.replace("!" , " ").upper())
print(sentence2)

#this  prints the new line
sentence= (sentence2.upper())

#This prints out the string backwards
print(sentence2[::-1])
