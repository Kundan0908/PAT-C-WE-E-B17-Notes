# Create a game to play guessing of numbers

# Define a range for guessing
# You need to ask for guesing number
# conditional check to validate the guess
# Add re-attempting

from random import randint

number = randint(1,50)
user_guess = input("Enter your guessed number between 1 - 50: ")
if user_guess == number:
    print("congratulations!!! You have guessed right!!!")
else:
    print(f"Try again, correct number was {number}")

# programming -> Solution is what you think in ur head -> Implement that same soln with programming logic that you know