import random
class GuessNumber:
    @staticmethod
    def guess_number():
        try:
            rand = random.randint(1, 10)
            while True:
                number = float(input("Enter number: "))

                if number > rand:
                    print(f"Need less")
                elif number < rand:
                    print("Need more")
                else:
                    print("You win!")
                    break
        except Exception as e:
            print(f"Error: {repr(e)}")

GuessNumber.guess_number()
