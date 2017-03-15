"""Treehouse number game"""
# safely make an int
# Limit the number of guesses
# too high message
# too low message
# play again

import random

def generate_secret():
    """Return random int"""
    print('firing')
    return random.randint(1, 10)

def main():
    """ Contains the main body of the app. """
    secret = generate_secret()
    guesses = 0
    while True:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        if guess == secret:
            print("You got it! My number was {}".format(secret))
            play_again = input("Do you want to play again? (Y/n): ")
            if play_again != "Y":
                print("Thanks for playing!")
                exit()
            else:
                main()
        elif guesses > 5:
            print("Unlucky, try again!")
        else:
            if guess < secret:
                print("You're too low!")
            else:
                print("You're too high!")
        guesses += 1

main()
