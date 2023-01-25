'''
A very rudimentary bot for 2048 on https://play2048.co/
1) start game
2) keep sending up, down, left, right keystrokes 
3) restart game
'''
from sys import exit
try:
    from selenium import webdriver
except ImportError:
    exit('This program requires selenium.')

if __name__ == '__main__':
    main()