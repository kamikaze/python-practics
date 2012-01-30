#!/usr/bin/env python
# -*- coding: utf-8 -*-

result = None

def magic_mul(a, b):
    global result
    result = a * b

def magic_div(a, b):
    global result

    if b != 0:
        result = a / b

def magic_sum(a, b):
    global result
    result = a + b

def magic_diff(a, b):
    global result
    result = a - b

def main():
    num1 = input('Please enter first number: ')
    num1 = int(num1)
    num2 = input('Please enter second number: ')
    num2 = int(num2)

    oper_symbol = None
    while oper_symbol != '*' and oper_symbol != '/' and oper_symbol != '+' and oper_symbol != '-':
        oper_symbol = input('Please enter an operation you want to do: ')

    if oper_symbol == '*':
        magic_mul(num1, num2)
    elif oper_symbol == '/':
        magic_div(num1, num2)
    elif oper_symbol == '+':
        magic_sum(num1, num2)
    elif oper_symbol == '-':
        magic_diff(num1, num2)

    print(result)

if __name__ == '__main__':
    main()
