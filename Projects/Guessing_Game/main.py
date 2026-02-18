from random import randint

class GuessingGame:
    def play(self, a, b):
        count_guesses = 0
        guessing_number = randint(a, b)
        while True:
            player_number = int(input('Guess: '))
            if player_number > guessing_number:
                print(f"{player_number} -> Too high")
                count_guesses += 1
                continue

            elif player_number < guessing_number:
                print(f"{player_number} -> Too low")
                count_guesses += 1
                continue

            else:
                count_guesses += 1
                break

        return f"{player_number} -> Correct!\nTotal Guesses: {count_guesses}"

play = GuessingGame()
print(play.play(1, 1000))