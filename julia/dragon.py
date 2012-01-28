#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.', end='\n\n')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2)')

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...', end='\n\n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':

          displayIntro()

          caveNumber = chooseCave()

          checkCave(caveNumber)

          playAgain = input('Do you want to play again? (yes or no)')

if __name__ == '__main__':
    main()
