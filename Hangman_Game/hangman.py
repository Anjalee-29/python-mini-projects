import random

def hangman():
    word = random.choice(["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guesses_made = ''

    while turns > 0:
        # Build the display string with consistent spacing
        display = " ".join(letter if letter in guesses_made else "_" for letter in word)

        if "_" not in display:
            print(display)
            print("You win!")
            break

        print("Guess the word:", display)
        guess = input("> ").casefold().strip()

        if guess not in valid_letters:
            print("Enter a valid character (a-z only)")
            continue

        if guess in guesses_made:
            print(f"You already guessed '{guess}', try another letter.")
            continue

        guesses_made += guess

        if guess not in word:
            turns -= 1

        if turns == 9:
            print("9 turns left")
            print("  --------  ")
        elif turns == 8:
            print("8 turns left")
            print("  ---------  ")
            print("      O      ")
        elif turns == 7:
            print("7 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
        elif turns == 6:
            print("6 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("     /       ")
        elif turns == 5:
            print("5 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print(r"    / \      ")
        elif turns == 4:
            print("4 turns left")
            print("  ---------  ")
            print(r"    \ O      ")
            print("      |      ")
            print(r"    / \      ")
        elif turns == 3:
            print("3 turns left")
            print("  ---------  ")
            print(r"   \ O /     ")
            print("      |      ")
            print(r"    / \      ")
        elif turns == 2:
            print("2 turns left")
            print("  ---------  ")
            print(r"   \ O /|    ")
            print("      |      ")
            print(r"    / \      ")
        elif turns == 1:
            print("1 turn left — Last breaths counting. Take care!")
            print("  ---------  ")
            print(r"   \ O_|/    ")
            print("      |      ")
            print(r"    / \      ")
        elif turns == 0:
            print("You lose!")
            print("You let a kind man die.")
            print(f"The word was: {word}")
            print("  ---------  ")
            print("      O_|    ")
            print(r"    /|\      ")
            print(r"    / \      ")
            break

    print()

name = input("Enter your name: ")
print(f"Welcome, {name}!")
print("=" * 40)
print("Try to guess the word in less than 10 attempts.")
hangman()
