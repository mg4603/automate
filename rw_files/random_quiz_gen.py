'''
1) create 35 quizzes
2) create 50 mcq for each quiz, in random order
3) provide the correct answer and 3 wrong answers
4) write quizzes to 35 text files
5) write answer keys to 35 text files.
'''
from random import shuffle, choice
from sys import exit
try:
    from pyinputplus import inputNum
except ImportError:
    exit('This program requires pyinputplus')
from pathlib import Path

qa_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

def get_answer_options(answers, correct_answer):
    answer_options = [correct_answer]
    while len(answer_options) < 4:
        answer_option = choice(answers)
        if answer_option not in answer_options:
            answer_options.append(answer_option)
    shuffle(answer_options)
    return answer_options

def get_quiz(qa_dict, num):
    answers = list(qa_dict.values())
    questions = list(qa_dict.keys())
    shuffle(questions)

    quiz_str = '{}:\n\n{}:\n\n{}:\n\n{}{} (Form {})\n\n'.format(
        'Name',
        'Date',
        'Period',
        ' ' * 20,
        'State Capitals Quiz',
        num
    )
    ans_str = ''
    for i, question in enumerate(questions):
        correct_answer = qa_dict[question]
        answer_options = get_answer_options(answers, correct_answer)
        quiz_str += '{}. What is the capital of {}?\n'.format(
            i + 1,
            question
        )
        for j, answer_option in enumerate(answer_options):
            quiz_str += '{}. {}\n'.format('ABCD'[j], answer_option)
        quiz_str += '\n'
        ans_str += '{}. {}\n'.format(
            i + 1, 'ABCD'[answer_options.index(correct_answer)]
        )
    return quiz_str, ans_str


def main():
    cwd = Path('.')
    output_dir = cwd / 'quizzes'
    output_dir.mkdir(parents=True, exist_ok=True)

    print('Enter number of quizzes')
    num_of_quizzes = inputNum(min=1, prompt='> ')
    for i in range(num_of_quizzes):
        quiz, answers = get_quiz(qa_dict, i + 1)
        quiz_file = output_dir / ('quiz_{}.txt'.format(i + 1))
        answer_file = output_dir / ('answer_{}.txt'.format(i + 1))
        with quiz_file.open('w') as file:
            file.write(quiz)
        with answer_file.open('w') as file:
            file.write(answers)

from pprint import pprint
if __name__ == '__main__':
    main()