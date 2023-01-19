from time import sleep

DELAY = 0.1

def main():
    indent  = 0
    indent_increasing = True

    while True:
        sleep(DELAY)
        print('{}*******'.format(' ' * indent))
        sleep()
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = not indent_increasing
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = not indent_increasing


