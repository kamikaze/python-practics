#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Julija
#
# Created:     23/01/2012
# Copyright:   (c) Julija 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    x = input('Please input a word (enter \"end\" to finish): ')
    print (x)
    stop_word = 'end'
    while stop_word != x:
        input('Please input a word (enter \"end\" to finish): ')

        if x == stop_word:
            break
            print('You have entered such words: ')

if __name__ == '__main__':
    main()
