'''
1) get input_file name
2) process input file
3) query wherever adjective, noun, adverb or verb are found
4) replace with queried values
5) print result and write to outfile
'''
from pathlib import Path
from sys import exit
try:
    from pyinputplus import inputStr
except ImportError:
    exit('This program requires pyinputplus to run.')

def main():
    print('Mad Libs')
    in_file = get_input_file()
    with in_file.open('r') as file:
        mad_lib_in = file.read()
    
    mad_lib_out = ''
    for word in mad_lib_in.split(' '):
        if word == 'ADJECTIVE':
            mad_lib_out += inputStr(prompt='Enter an adjective:\n')
        elif word == 'NOUN':
            mad_lib_out += inputStr(prompt='Enter a noun:\n')
        elif word == 'VERB':
            mad_lib_out += inputStr(prompt='Enter a verb:\n')
        elif word == 'ADVERB':
            mad_lib_out += inputStr(prompt='Enter an adverb:\n')
        else:
            mad_lib_out += word
            
    out_file_name = inputStr('Enter output file name:\n')
    print(mad_lib_out)
    
    with Path(out_file_name).open('w') as out_file:
        out_file.write(mad_lib_out)
    
if __name__ == '__main__':
    main()