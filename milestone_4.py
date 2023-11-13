import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            print(f"Good guess! {guess} is in the word")    
            self.num_letters -= 1      
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Enter a word: ")
            if not guess.isalpha() or len(guess) != 1:
                 print("Invalid letter. Please enter a single alphabetic letter")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        if self.num_letters == 0:
            print(f"Many congratulations, you have won the game. The word was: {''.join(self.word_guessed)}")
        else:
            print(f"You lose! Game Over! the word was, {self.word}")

word_list = ["tangerine", "apple", "pineapple", "plum", "banana"]
game = Hangman(word_list)
game.ask_for_input()

 