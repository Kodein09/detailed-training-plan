# from random import randrange
#
# class MiniGame:
#     def __init__(self):
#         self.hearts = 3
#         self.random_number = randrange(5)
#
#     def mini_game_random(self):
#         print(f"\nRemember, you have only 3 hearts.\nGood luck.")
#         while True:
#             number = int(input("Enter the number: "))
#             if number > self.random_number:
#                 if number != self.random_number:
#                     self.hearts -= 1
#                 if self.hearts == 0:
#                     print(f"GAME OVER\nYOU DIED...")
#                     break
#                 print(f"Wrong, {self.hearts} hearts left. Try not to fail.\nNumber {number} is more than guessed number, try again.")
#
#             elif number < self.random_number:
#                 if number != self.random_number:
#                     self.hearts -= 1
#                 if self.hearts == 1:
#                     print(f"WRONG\n{self.hearts} HEART LEFT!\nNumber {number} is less than guessed number, try again.")
#                 continue
#             else:
#                 print(f"You win!\nGuessed number is: {self.random_number}.")
#                 break
#         return "The end."
#
# minigame = MiniGame()
# minigame.mini_game_random()


from random import randrange as rr

class MiniGame:
    print("This is my mini-game, it's all about a guessing the numbers, I hope you like it, enjoy!")
    def __init__(self):
        self.hearts = 3
        self.random_number = rr(5)

    def guess_number(self):
        choice = input("You can choose your own level, type from '1' to '10'\nLevel: ")
        def level_one():
            print(f">>READY\n>>SET\n>>GAME\n>>If you need to exit type: 'exit 'or 'Exit'\n>>Mode: Easy mode")
            while True:
                number = (input(">>Enter the number: "))

                if number == self.random_number:
                    print("You win")
                    break

                elif number != self.random_number:
                    if number == 'exit' or number == 'Exit':
                        MiniGame.guess_number(self)

                    if number == "" and " ":
                        print("You need to enter a number.")
                        continue

                    self.hearts -= 1
                    print(f"{self.hearts} hearts left")

                    if int(number) > self.random_number:
                        print(f"Guessed number is less than your's {number}")

                    elif int(number) < self.random_number:
                        print(f"Guessed number is more than your's {number}")

                    if self.hearts == 0:
                        print("Game over")
                        try_again = input("You can try again if you want, print: 'again' or 'leave': ")
                        if try_again == 'again':
                            self.hearts = 3
                            continue
                        elif try_again == 'leave':
                            MiniGame.guess_number(self)
        def level_two():
            print("Level 2")
            pass

        def level_three():
            print("Level 3")
            pass

        def level_four():
            print("Level 4")
            pass

        levels = {
            '1': level_one,
            '2': level_two,
            '3': level_three,
            '4': level_four,
        }
        level_func = levels.get(choice)
        if level_func:
            level_func()
        else:
            print("Invalid level.")


game = MiniGame()
game.guess_number()
