'''
1) create 35 quizzes
2) create 50 mcq for each quiz, in random order
3) provide the correct answer and 3 wrong answers
4) write quizzes to 35 text files
5) write answer keys to 35 text files.
'''
from sys import exit
try:
    from pyinputplus import inputNum
except ImportError:
    exit('This program requires pyinputplus')
from pathlib import Path

def main():
    cwd = Path('.')
    output_dir = cwd / 'quizzes'
    output_dir.mkdir(parents=True)

    print('Enter number of quizzes')
    num_of_quizzes = inputNum(min=1, prompt='> ')
    for i in range(num_of_quizzes):
        quiz, answers = get_quiz(qa_dict)
        quiz_file = output_dir / ('quiz_{}.txt'.format(i + 1))
        answer_file = output_dir / ('answer_{}.txt'.format(i + 1))
        with quiz_file.open('w') as file:
            file.write(quiz)
        with answer_file.open('w') as file:
            file.write(answers)


if __name__ == '__main__':
    main()