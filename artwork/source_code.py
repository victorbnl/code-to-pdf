"""
Guess the number game.
"""

import random

if __name__ == '__main__':

    number = random.randint(1, 100)

    while True:
        attempt = int(input("Guess the number: "))

        if attempt == number:
            print("You won, congratulations!")
            break

        elif attempt > number:
            print("Too big")

        elif attempt < number:
            print("Too small")
