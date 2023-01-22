'''
1) get input_file name
2) process input file
3) query wherever adjective, noun, adverb or verb are found
4) replace with queried values
5) print result and write to outfile
'''
from pathlib import Path
from re import sub
from sys import exit
try:
    from pyinputplus import inputStr
except ImportError:
    exit('This program requires pyinputplus to run.')

def get_input_file():
    while True:
        in_file_name = input('Enter input file name:\n')
        if Path(in_file_name).exists():
            return Path(in_file_name)
        print('File doesn\'t exist.\n')

def main():
    print('Mad Libs')
    in_file = get_input_file()
    with in_file.open('r') as file:
        mad_lib_in = file.read()
    
    mad_lib_out = []
    for word in mad_lib_in.split(' '):
        if 'ADJECTIVE' in word:
            adjective = inputStr(prompt='Enter an adjective:\n')
            new_word = sub('ADJECTIVE', adjective, word)
        elif 'NOUN' in word:
            noun = inputStr(prompt='Enter a noun:\n')
            new_word = sub('NOUN', noun, word)
        elif 'VERB' in word:
            verb = inputStr(prompt='Enter a verb:\n')
            new_word = sub('VERB', verb, word)
        elif 'ADVERB' in word:
            adverb = inputStr(prompt='Enter an adverb:\n')
            new_word = sub('ADVERB', adverb, word)
        else:
            new_word = word
        mad_lib_out.append(new_word)
    mad_lib_out = ' '.join(mad_lib_out)
            
    out_file_name = inputStr('Enter output file name:\n')
    print(mad_lib_out)

    with Path(out_file_name).open('w') as out_file:
        out_file.write(mad_lib_out)
    
if __name__ == '__main__':
    main()