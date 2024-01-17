import random

class Hangman:
    """
    A class representing the Hangman game.

    Attributes:
    - word_list: List of words to choose from.
    - num_lives: Number of lives the player starts with.
    - word: The randomly chosen word for the current game.
    - word_guessed: List representing the current state of the guessed word.
    - num_letters: Number of unique letters in the chosen word.
    - list_of_guesses: List to store guessed letters.
    """

    def __init__(self, word_list, num_lives=5):
        """
        This initiates a new instance of the Hangman Class

        Parameters:
        - word_list (list): List of words to choose from.
        - num_lives (int): Number of lives the player starts with.
        """
        #Randomly chooses a word from the list and initialize game attributes
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates game state accordingly.

        Parameters:
        - guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            #Update the word_guessed list if the guessed letter is correct
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            print(f"Good guess! {guess} is in the word")    
            self.num_letters -= 1      
        else:
            #Decreases the number of lives
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """
        Prompts the user for input and processes the guessed letter.
        """
        while self.num_lives > 0 and self.num_letters > 0:
            #Gets user input
            guess = input("Enter a word: ")
            if not guess.isalpha() or len(guess) != 1:
                 print("Invalid letter. Please enter a single alphabetic letter")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                #Processes the guessed letter
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def display_game_result(self):
        """
        Displays the result of the Hangman game.
        """
        if self.num_letters == 0:
            #Prints Congratulation if player wins
            print(f"Many congratulations, you have won the game. The word was: {''.join(self.word_guessed)}")
        else:
            print(f"You lose! Game Over! The word was: {self.word}")

def play_game(word_list):
    """
    Plays the Hangman game.

    Parameters:
    - word_list (list): List of words to choose from.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    #Start the game by running user input
    game.ask_for_input()

    #Display the result of the game
    game.display_game_result()

word_list = ["tangerine", "apple", "pineapple", "plum", "banana"]
play_game(word_list)

