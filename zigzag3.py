from time import sleep
from sys import exit

DELAY = 0.1

def main():
    indent  = 0
    indent_increasing = True

    while True:
        print('{}*******'.format(' ' * indent))
        sleep(DELAY)
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = not indent_increasing
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = not indent_increasing


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()