#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Julija
#
# Created:     21/01/2012
# Copyright:   (c) Julija 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def magic(a=10, b=5):
    return a-b

def main():
    print('a', 'b', sep='+', end='=')
    print('c')

    input('Enter your name: ')

    cnt = input('Enter the number: ')
    cnt = int(cnt)
    i = 0

    while i < cnt:
        print('Hello')
        i = i+1



if __name__ == '__main__':
    main()
