"""Letter guessing game"""
# make a list of words
# pick a random word
# draw spaces
# take guess
# draw guessed letters and strikes
# print out win/lose
import os
import random
import sys

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

def clear():
    """Clear the screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret):
    """draw out the words"""
    clear()
    print('Strikes: {}/7\n'. format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end='')
    print('\n\n')

    for letter in secret:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
    print('')

def get_guess(bad_guesses, good_guesses):
    """gets the guess"""
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that one!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    secret = random.choice(WORDS)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret)
        guess = get_guess(bad_guesses, good_guesses)

        while True:
            start = input("Press enter to start, or enter q to quit")
            if start.upper() == 'Q':
                break
            secret = random.choice(WORDS)
            bad_guesses = []
            good_guesses = []

            while len(bad_guesses) < 8 and len(good_guesses) != len(list(secret)):



                if guess in secret:
                    good_guesses.append(guess)
                    if len(good_guesses) == len(secret):
                        print('You won! The word was {}'.format(secret))
                else:
                    bad_guesses.append(guess)

main()
