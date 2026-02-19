import random

class WordGuessingGame:
    def play(self, w):
        word = random.choice(words)
        total_guesses = 0
        failed = 0
        turns = 12
        seen = []

        user = input("What is your name?\n")
        print(f"Good luck, {user}!")
        while turns > 0:
            turns -= 1
            guessing = input("Guess a character: ")
            total_guesses += 1
            for char in word:
                if char == guessing:
                    print(char, end="\n")
                else:
                    print("_")


        print(f"You run out of turns: {turns}")

words = ['decomposition', 'computer', 'redemption', 'river', 'rock', 'reverse', 'water', 'fan', 'science']
gg = WordGuessingGame()
gg.play(words)