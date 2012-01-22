#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    # Privetstvie programmi
    print('Hello, I am your first programm!')
    # Znakomstvo s poljzovatelem i peremennaja, kotoruju vvodit poljzovatelj, v dannom sluchae imja
    user_name = input('What is your name: ')
    # Statement (ne znaju kak nazvatj, chto-to vrode konstanti)
    name = 'Oleg'
    # Uslovie, sravnenie vvedennoj peremennoj so Statementom
    if user_name == name:
        # Rezuljtat, kotorij programma vivodit na ekran, pri vipolnenii visheupomjanutogo uslovija
        print('Nice to meet you, ' + user_name + ', Have a nice day!!!')
    # Uslovie, pri kotorom vvedennaj peremennaja ne sovpadaet so Statementom
    else:
        # Rezuljtat, kotorij programma vivodit na ekran, pri vipolnenii visheukazannogo uslovija
        print('Nice to meet you, ' + user_name + '!')
    # Prosjba programmi vvesti chislo i peremennaja, kotoruju vvodit poljzovatelj, v dannom sluchae chislo
    num = input(user_name + ', enter the number please: ')
    # Statement
    my_number = 20
    user_number = int(num)
    # Uslovie
    if user_number > my_number:
       # Rezuljtat na ekrane, pri vipolnenii visheukazannogo uslovija
       print('This number is greater than 20!')
    # Uslovie
    elif user_number < my_number:
        # Rezuljtat na ekrane, pri vipolnenii visheukazannogo uslovija
        print('This number is less than 20!')
    else:
        print('This is exactly 20!')


#detecting if file is called
if __name__ == '__main__':
    main()
