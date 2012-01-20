#!/usr/bin/env python

def main():
    # Privetstvie programmi
    print('Hello, I am your first programm!')
    # Znakomstvo s poljzovatelem
    print('What is your name?')
    # Peremennaja, kotoruju vvodit poljzovatelj, v dannom sluchae imja
    yourName = input()
    # Statement (ne znaju kak nazvatj, chto-to vrode konstanti)
    name = 'Oleg'
    # Uslovie, sravnenie vvedennoj peremennoj so Statementom
    if yourName == name:
        # Rezuljtat, kotorij programma vivodit na ekran, pri vipolnenii visheupomjanutogo uslovija
        print('Nice to meet you, ' + yourName + ', Have a nice day!!!')
    # Uslovie, pri kotorom vvedennaj peremennaja ne sovpadaet so Statementom
    if yourName != name:
        # Rezuljtat, kotorij programma vivodit na ekran, pri vipolnenii visheukazannogo uslovija
        print('Nice to meet you, ' + yourName + '!')
    # Prosjba programmi vvesti chislo
    print(yourName + ', enter the number please!')
    # Peremennaja, kotoruju vvodit poljzovatelj, v dannom sluchae chislo
    num = input()
    # Statement
    myNumber = 20
    yourNumber = int(num)
    # Uslovie
    if yourNumber > myNumber:
       # Rezuljtat na ekrane, pri vipolnenii visheukazannogo uslovija
       print('This number is greater than 20!')
    # Uslovie
    elif yourNumber < myNumber:
        # Rezuljtat na ekrane, pri vipolnenii visheukazannogo uslovija
        print('This number is less than 20!')
    else:
        print('This is exactly 20!')


#detecting if file is called
if __name__ == '__main__':
    main()
