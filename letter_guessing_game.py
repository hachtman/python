"""Letter guessing game"""
# make a list of words
# pick a random word
# draw spaces
# take guess
# draw guessed letters and strikes
# print out win/lose

import random

WORDS = [
    'apple',
    'kiwi',
    'banana',
    'kumquat',
    'grapefruit',
    'orange',
    'lemon',
    'melon'
]

def main():
    """main function to run the game"""
    while True:
        start = input("Press enter to start, or enter q to quit")
        if start.upper() == 'Q':
            break
        secret = random.choice(WORDS)
        bad_guesses = []
        good_guesses = []

        while len(bad_guesses) < 8 and len(good_guesses) != len(list(secret)):
            for letter in secret:
                if letter in good_guesses:
                    print(letter, end='')
                else:
                    print('_', end='')

            print('')
            print('Strikes: {}/7\n'. format(len(bad_guesses)))

            guess = input('Guess a letter: ').lower()
            if len(guess) != 1:
                print("You can only guess a single letter!")
                continue
            elif guess in bad_guesses or guess in good_guesses:
                print("You've already guessed that one!")
                continue
            elif not guess.isalpha():
                print("You can only guess letters!")
                continue

            if guess in secret:
                good_guesses.append(guess)
                if len(good_guesses) == len(secret):
                    print('You won! The word was {}'.format(secret))
            else:
                bad_guesses.append(guess)

main()
