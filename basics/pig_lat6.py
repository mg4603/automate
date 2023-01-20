
def main():
    print('Enter message to translate to Pig Latin:')
    msg = input('> ')
    translated_message = translate_to_pig_latin(msg)
    print()
    print('Translated Message:')
    print(translated_message)

if __name__ == '__main__':
    main()