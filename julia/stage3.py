#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def my_sum(a, b):
    return a + b

def my_mul(a, b):
    return a * b

def my_random(a, b):
    c = random.random()
    return a * b + c

def my_greeting():
    name = input('What is your name: ')
    return name

def my_magic_greeting(name, time_of_day):
    greeting_user = print('Good ' + time_of_day + ', ' + name + '!')
    return greeting_user

def main():
    result = my_sum(2, 3)
    print(result)

    result = my_mul(5, 3)
    print(result)

    result = my_random(4, 6)
    print(result)

    #result = my_greeting()
    my_magic = my_greeting
    result = my_magic()
    print(result)

    result = my_magic_greeting('Julia', 'morning')
    print(result)

    result = my_magic_greeting(time_of_day = 'morning', name = 'Julia')
    print(result)

if __name__ == '__main__':
   main()