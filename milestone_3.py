
import random

def check_guess(guess, word):
    guess = guess.lower()
    while True:    
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                print(f"Good guess! {guess} is in the word")           
            else:
                print(f"Sorry, {guess} is not in the word. Try again")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    print("Good Guess. The word you guessed is: ", guess)

word_list = ["tangerine", "apple", "pineapple", "plum", "banana"]
word = random.choice(word_list)

user_guess = input(str("Enter a letter: "))

check_guess(user_guess, word)



def ask_for_input():
     while True:
            user_guess = input(str("Enter a letter: ")).lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                check_guess(user_guess,word)
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

            print("Good Guess. The word you guessed is: ", user_guess)

ask_for_input()

