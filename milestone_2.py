import random
word_list = ["tangerine", "apple", "pineapple", "plum", "banana"]
word = random.choice(word_list)
print(word)

guess = input(str("Enter a letter: "))
if len(guess) == 1 and guess.isalpha():
    print("Good Guess")
else:
    print("Oops! That is not a valid input.")

