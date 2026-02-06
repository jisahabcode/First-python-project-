#my first python project
import random

num = random.randint(1, 10)

guess = int(input("Guess number (1-10): "))

if guess == num:
    print("You Win 🎉")
else:
    print("You Lose 😢")
    print("Number was:", num)