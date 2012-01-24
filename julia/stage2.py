#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import random

    guesses_taken = 0
    print('Hello! What is your name?')
    user_name = input()

    number = random.randint(1, 20)
    print('Well, ' + user_name + ' I am thinking of a number between 1 and 20.')

    while guesses_taken < 6:
        print('Take a guess.')
        guess = input()
        guess = int(guess)

        guesses_taken = guesses_taken + 1

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + user_name + '! You guessed my number in ' + guesses_taken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)


if __name__ == '__main__':
    main()
