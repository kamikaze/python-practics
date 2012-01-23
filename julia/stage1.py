#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    stop_word = 'end'
    x = total = input('Please input a word (enter "end" to finish): ')

    while x != stop_word:
        x = input('Please input a word (enter "end" to finish): ')
        total = total + ', ' + x

    print('You have entered such words: ' + total)

if __name__ == '__main__':
    main()
