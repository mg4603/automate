def translate_to_pig_latin(msg):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    msg = msg.split(' ')
    pig_latin = []
    for word in msg:
        prefix_non_letters = ''
        suffix_non_letters = ''
        prefix_consonants = ''
        is_upper = word.isupper()
        start_upper = word[0].isupper()


        for symbol in word:
            if not symbol.isalpha():
                prefix_non_letters += symbol
            elif symbol.lower() not in vowels:
                prefix_consonants += symbol
            else:
                break
        
        for i in range(len(word) - 1, -1, -1):
            if not word[i].isalpha():
                suffix_non_letters = word[i] + suffix_non_letters
            else:
                break
        
        if len(prefix_non_letters + suffix_non_letters) == len(word):
            pig_latin.append(word)
            continue
        elif len(prefix_non_letters) == len(suffix_non_letters) == len(word):
            pig_latin.append(word)
            continue
        
        if len(prefix_consonants + prefix_non_letters):
            if len(suffix_non_letters) > 0:
                new_word = word[
                        len(prefix_consonants + prefix_non_letters): 
                        -len(suffix_non_letters)
                    ].lower()
            else:
                new_word = word[len(prefix_consonants + prefix_non_letters):]

            
            
            new_word += prefix_non_letters + prefix_consonants + 'ay' +\
                 suffix_non_letters
            new_word = new_word.lower()
            
            if is_upper:
                new_word = new_word.upper()
            elif start_upper:
                new_word = new_word.title()
            pig_latin.append(new_word)
        else:
            if len(suffix_non_letters) > 0:
                new_word = word[:-len(suffix_non_letters)] + 'yay' + suffix_non_letters            
            else:
                new_word = word +  'yay'

            new_word = new_word.lower()

            if is_upper:
                pig_latin.append(new_word.upper())
                continue
            elif start_upper:
                pig_latin.append(new_word.title())
            else:
                pig_latin.append(new_word)

    return ' '.join(pig_latin)
                
            

def main():
    print('Enter message to translate to Pig Latin:')
    msg = input('> ')
    translated_message = translate_to_pig_latin(msg)
    print()
    print('Translated Message:')
    print(translated_message)

if __name__ == '__main__':
    main()