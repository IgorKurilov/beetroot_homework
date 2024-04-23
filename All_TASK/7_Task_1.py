# writen by  Igor Kurilov
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 10: "))

# Check if the guess is correct and provide feedback
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the number was {secret_number}. Try again next time!")