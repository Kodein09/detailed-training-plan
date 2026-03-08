import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      "Rock vs Paper -> Paper wins\n"
      "Rock vs Scissors -> Rock wins\n"
      "Scissors vs Paper -> Scissors wins")

def rps():
    while True:
        print("Enter your choice between 1 and 3 where\n"
              "1 -> Paper\n"
              "2 -> Rock\n"
              "3 -> Scissors")

        choice = int(input("Type your choice: "))
        while choice < 1 or choice > 3:
            choice = int(input("Please, enter a valid choice: "))

        if choice == 1:
            choice_name = 'Paper'
        elif choice == 2:
            choice_name = 'Rock'
        else:
            choice_name = 'Scissors'

        print(f"Your choice is: {choice_name}\nNow it's Computer's turn...")
        comp_choice = random.randint(1,3)

        if comp_choice == 1:
            comp_choice_name = 'Paper'
        elif comp_choice == 2:
            comp_choice_name = 'Rock'
        else:
            comp_choice_name = 'Scissors'

        print(f"Computer choice is: {comp_choice_name}\n{choice_name} vs {comp_choice_name}")

        if choice == comp_choice:
            result = 'DRAW'
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Paper'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Rock'
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = 'Scissors'

        if result == 'DRAW':
            print("It's a tie!")
        elif result == choice_name:
            print("User wins!")
        else:
            print("Computer wins!")

        print("Do you want to play again? [Y/N]")
        ans = str(input().upper())
        if ans == 'N':
            break

rps()