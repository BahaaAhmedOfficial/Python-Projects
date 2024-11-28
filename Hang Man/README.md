# Hangman Game

This Python script is a simple implementation of the classic Hangman game. Players guess letters to reveal a hidden word, and if they make too many incorrect guesses, the hangman is "completed" and they lose the game.

## Features

- Draws a hangman graphic as the player makes incorrect guesses.
- Allows the player to input guesses and checks them against the word.
- Provides a definition of the word at the end of the game using the Dictionary API.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository**:
    ```
    bash
    git clone https://github.com/yourusername/hangman-game.git
    cd hangman-game
    ```

2. **Install the `requests` library**:
    ```
    bash
    pip install requests
    ```

3. **Create a `words.txt` file** in the project directory:
    - Open a text editor and add a list of words, one per line. For example:
      ```
      plaintext
      apple
      banana
      cherry
      date
      elderberry
      ```
    - Save this file as `words.txt` in `D:\\05 - Projects\\Python\\HangMan\\`.

## Usage

1. **Run the script**:
    ```
    bash
    python main.py
    ```

2. **Gameplay**:
    - The game will prompt you to guess letters one at a time.
    - The hangman graphic will update with each incorrect guess.
    - If you guess the word correctly before the hangman is completed, you win.
    - If the hangman is completed before you guess the word, you lose and the definition of the word is displayed.

## Functions

### `draw_the_hangman(wrong_count, word)`

Draws the hangman graphic based on the number of incorrect guesses.

- **Parameters**: 
  - `wrong_count` (int): Number of incorrect guesses.
  - `word` (str): The word being guessed.

### `get_player_guess(word, player_guess, guesses)`

Gets a guess from the player and updates the guessed letters.

- **Parameters**:
  - `word` (str): The word being guessed.
  - `player_guess` (list): List of correct guesses.
  - `guesses` (list): List of all guesses made.
- **Returns**:
  - `result` (list): A list containing two boolean values, indicating if the guess was correct and if it was a repeat.

### `print_word_state(word, player_guess)`

Prints the current state of the word being guessed.

- **Parameters**: 
  - `word` (str): The word being guessed.
  - `player_guess` (list): List of correct guesses.
- **Returns**:
  - `bool`: `True` if the entire word has been guessed, `False` otherwise.

### `get_word_details(word)`

Fetches and prints the definition of the word using the Dictionary API.

- **Parameters**: 
  - `word` (str): The word for which the definition is to be fetched.

### `main()`

Main function to run the Hangman game.

- **Reads a list of words from a file.**
- **Selects a random word for the game.**
- **Manages the game loop.**

## Notes

- Ensure your `words.txt` file contains a list of words with a minimum length of 3 characters.
- The script uses the Dictionary API to fetch word definitions.

---

Enjoy playing Hangman and expanding your vocabulary! 🎉
