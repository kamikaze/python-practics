#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():
    guesses_taken = 0
    user_name = input('Hello! What is your name?: ')

    number = random.randint(1, 20)
    print('Well, ' + user_name + ' I am thinking of a number between 1 and 20.')

    while guesses_taken < 6:
        guess = int(input('Take a guess: '))

        guesses_taken = guesses_taken + 1

        if guess < number:
           print('Your guess is too low.')
        elif guess > number:
           print('Your guess is too high.')
        else:
            break

    if guess == number:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + user_name + '! You guessed my number in ' + guesses_taken + ' guesses!')
    else:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)


if __name__ == '__main__':
    main()
