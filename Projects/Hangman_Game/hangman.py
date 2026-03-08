import random

some_fruits = ['apple', '', 'coconut', 'cherry', 'orange', 'watermelon', 'crimson', 'grape', 'melon', 'lemon', 'kivi']

def hangman(words):
    word = random.choice(words)
    print("HINT! The word is a fruit.\nGood luck and have fun!")
    turns = 6
    guesses = ''

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end="")
                failed += 1

        if failed == 0:
            print("You Win!")
            print(f"The word is: {word}")
            break

        character = str(input("\nType character: "))
        if len(character) > 1:
            print("You allowed type only single character and for that you get a penalty -1 turn")
            turns -= 1
            print(f"\nYou have {turns} more turns left")
            continue

        guesses += character

        if character not in word:
            turns -= 1
            print(f"\nYou have {turns} more turns left")

            if turns == 0:
                print("Game Over")

hangman(some_fruits)