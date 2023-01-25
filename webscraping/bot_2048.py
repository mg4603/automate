'''
A very rudimentary bot for 2048 on https://play2048.co/
1) start game
2) keep sending up, down, left, right keystrokes 
3) restart game
'''
from sys import exit
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
from random import choice
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
except ImportError:
    exit('This program requires selenium.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def main():
    browser = webdriver.Firefox()
    browser.get('https://play2048.co/')
    board_elem = browser.find_element(By.TAG_NAME, 'html')

    while True:
        key = choice([Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT])
        board_elem.send_keys(key)
        
if __name__ == '__main__':
    main()