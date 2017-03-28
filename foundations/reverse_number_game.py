"""A version where the computer guesses!"""

# Have the user select a number and store it in a variable
# Have the computer make a guess. If correct, end the game, ask the user too play again.
# If incorrect, have the user enter H for L for high or low
# Limit the computers guess range accordingly.

import random

def generate_guess(lower_bound, higher_bound):
    """Return random int"""
    return random.randint(lower_bound, higher_bound)

def main():
    """the main body of the game"""
    # init variables
    lower_bound = 1
    higher_bound = 10
    guess = generate_guess(1, 10)
    while True:
        try:
            secret = input("What should the computer guess? Enter a number between 1 and 10: ")
        except ValueError:
            print("{} isn't a number!".format(secret))
        while True:
            if int(guess) == int(secret):
                print("I guessed {}! Your number was {}! I win!".format(guess, secret))
                play_again = input("Do you want to play again? (Y/n)")
                if play_again != "Y":
                    print("Thanks for playing!")
                    exit()
                else:
                    main()
            elif int(guess) != int(secret):
                high_or_low = input("I guessed {}. Was it high or low? (H/L)".format(guess))
                print("G: {}, HB: {}, LB: {}".format(guess, higher_bound, lower_bound))
                if high_or_low == "H":
                    higher_bound = guess - 1
                    guess = generate_guess(lower_bound, higher_bound)
                elif high_or_low == "L":
                    lower_bound = guess + 1
                    guess = generate_guess(lower_bound, higher_bound)
                else:
                    print("Please try again: \n")
main()
