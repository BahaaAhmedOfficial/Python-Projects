import random
import requests

def draw_the_hangman(wrong_count, word):
    print("\n\n")
    print(" ============ ")
    print("   |         ")
    if wrong_count == 1:
        print("   O")
    if wrong_count == 2:
        print("   O")
        print("   |")
    if wrong_count == 3:
        print("   O")
        print("  /|")
    if wrong_count == 4:
        print("   O")
        print("  /|\\")
    if wrong_count == 5:
        print("   O")
        print("  /|\\")
        print("  /")
    if wrong_count == 6:
        print("   O")
        print("  /|\\")
        print("  / \\")
        print("You lose! ha ha ha")
        print(f"The word was '{word}'")
        get_word_details(word)
        exit(0)
    print("\n\n")

def get_player_guess(word, player_guess, guesses):
    letter_guess = input("Please enter your guess: ")
    guessed_letter = letter_guess[0]
    result = [False, False]
    if guessed_letter in guesses:
        print("That letter has already been guessed. Please choose a new letter.")
        result[0] = False  # guess was incorrect
        result[1] = True   # guess was a repeat
    else:
        player_guess.append(guessed_letter)
        guesses.append(guessed_letter)
        result[0] = guessed_letter in word  # guess was correct
        result[1] = False  # guess was not a repeat
    return result

def print_word_state(word, player_guess):
    correct_count = 0
    for i in range(len(word)):
        if word[i] in player_guess:
            print(word[i], end='')
            correct_count += 1
        else:
            print('-', end='')
    print()
    return correct_count == len(word)  # Returns true or false

def get_word_details(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()

    if response.status_code == 200 and 'meanings' in data[0] and 'definitions' in data[0]['meanings'][0] and 'definition' in data[0]['meanings'][0]['definitions'][0]:
        print(f"\nWord: {word}")
        print(f"Definition: {data[0]['meanings'][0]['definitions'][0]['definition']}\n")
    else:
        print(f"No definition found for the word: {word}")

def main():
    try:
        with open("D:\\05 - Projects\\Python\\HangMan\\words.txt", 'r',
                  encoding='utf-8') as f:
            words = [line.strip() for line in f]
    except Exception as e:
        print(f"An error occurred: {e}")

    long_words = [word for word in words if len(word) >= 3]
    word = random.choice(long_words)  # Gets a new random word

    player_guess = []
    guesses = []
    wrong_count = 0

    while True:
        draw_the_hangman(wrong_count, word)
        print_word_state(word, player_guess)
        print("Guessed letters are: ", guesses)

        guess_result = get_player_guess(word, player_guess, guesses)
        if not guess_result[0] and not guess_result[1]:
            wrong_count += 1
        if print_word_state(word, player_guess):  # if it returns true
            print("You won!! 🎉🎉🎉")
            get_word_details(word)
            break

if __name__ == "__main__":
    main()
