# Project Title: Hangman

## Table of Contents
- [Description](#description)
- [Project Goals](#project-goals)
- [Milestone 5: Completed Game](#milestone-5-completed-game)
- [Lessons Learnt](#lessons-learnt)
- [Installation Instructions](#installation-instructions)

## Description
The Hangman Game is a simple text-based implementation of the classic word-guessing game. The aim of the project is to provide an entertaining, easy to use and interactive experience for users as they attempt to guess a word taht is randomly selected within a specified number of lives.

## Project Goals
1. Create a user-friendly Hangman game in Python.
2. Implement game logic, including word selection, guessing, and feedback.
3. Enhance programming python skills through project development.

## Milestone 5: Completed Game
In Milestone 5, the game is completed, and players can run the script to enjoy the Hangman experience. Key methods/functions include:

- `__init__(self, word_list, num_lives=5)`: Initializes a new instance of the Hangman class.
```python
 def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
```
- `check_guess(self, guess)`: Checks if the guessed letter is in the word and updates game state accordingly.
```python
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
```
- `ask_for_input(self)`: code block prompts the user for input and processes the guessed letter.
```python
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
```
- `display_game_result(self)`: Displays the result of the Hangman game.
```python
def display_game_result(self):
        if self.num_letters == 0:
            print(f"Many congratulations, you have won the game. The word was: {''.join(self.word_guessed)}")
        else:
            print(f"You lose! Game Over! The word was: {self.word}")
```

## Lessons Learnt
Throughout the duration of this project, I gained hands-on experience in:

- Python object-oriented programming.
- User input validation and handling.
- Game logic and state management.
- Code organization and structure.
- Version control using Git

## Installation Instructions
To run the Hangman Game on your machine, follow these steps:

1. Clone the repository to your local machine.
   * git clone https://github.com/Tawanda23/hangman923.git

2. Navigate to the project directory of your choice.

3. **Install required dependencies:**

4. Run the game script - ``` Milestone 5```

The game will start, and you can begin guessing the word.

5. **Follow on-screen instructions:**
- Enter a single letter when prompted.
- The game will provide feedback on your guesses.
- Keep guessing until you either guess the word or run out of lives.

