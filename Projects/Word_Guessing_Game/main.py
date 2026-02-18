import random

class WordGuessingGame:
    def play(self, words):
        word = random.choice(words)
        total_guesses = 0
        turns = 12
        

