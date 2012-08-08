#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 5

def main():
    global a
    #print(a)
    a = 7

if __name__ == '__main__':
    a = 6
    main()
    print(a)
