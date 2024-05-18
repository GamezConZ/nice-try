# This a simple portofolio project to showcase python skills under the Codecademy lessons
# It's going to be a game questionaire for friends, with a minimum of two players
# One or more friends write a personal questions quiz and the others have to guess the answer
# (Based on losing the apartment scene on Friends)
# IDEAS List:
# Running the program to specify if the user is going to create or answer the questions.
# Input the questions creator's data and funcionality (multiple choice - boolean)
# Create the questions based on what the user specified
# Save the questions to a json file
# Running the program as an answerer
# Input the answerer's data and functionality
# loading the json file
# Asking the question
# Returning the results
import random

class User:
    def __init__(self, username, creator = False):
        self.username = username
        self.creator = creator
        self.correct_answers = 0
        self.wrong_answers = 0
    def __repr__(self):
        return 'User'

class Question:
    # Define a question with its type, and in case of multiple options receives a list of options
    def __init__(self, question, type_of_question, true_or_false = False, options = []):
        self.question = question
        self.type_of_question = type_of_question
        self.options = options
        self.true_or_false = true_or_false
    def __repr__(self):
        return 'Question'
    
    # .ask() prints the question
    def ask(self):
        print('\n')
        print('Question: ')
        print(self.question)
    
    # .answer() checks if the provided answer is correct or not
    # It prints the result and adds the record to the user
    def answers(self, user):
        if self.true_or_false:
            choice = input('Is it True or False?: (T/F): ').upper()
            if choice == 'T':
                print('Correct!')
                print('\n')
                user.correct_answers += 1
            else:
                print('Incorrect!')
                print('\n')
                user.wrong_answers += 1
        else:
            # randomly prints the options
            num = 0
            correct_num = 0
            num_string = ''
            list_len = len(self.options)
            random_list = random.sample(range(0, list_len), list_len)
            for i in random_list:
                num += 1
                print(f"{num}.- {self.options[i][0]}")
                if self.options[i][1]:
                    correct_num = num
                num_string += f'{num} - '
            choice = int(input(f'Choose between options {num_string}: '))
            if choice == correct_num:
                print('Correct!')
                print('\n')
                user.correct_answers += 1
            else:
                print('Incorrect!')
                print('\n')
                user.wrong_answers += 1

def create_user():
    print('###################################')
    print('###################################')
    print('Welcome!')
    print('Let\'s set you up into the program')
    username = input('Please provide your username: ')
    creator = False
    role = input('Do you want to create questions(Q) or start answering(A)? (Q/A):').upper()
    if role == 'Q':
        creator = True
    return User(username, creator)

def create_questions():
    questions = []
    while True:
        print('###################################')
        print('###################################')
        print('\n')
        question_type = input('Do you want to create a multiple choice(M) or True/False(T) question? (M/T): ').upper()

        if question_type == 'T':
            question_sentence = input('Enter the question: ')
            question_answer = input('Is it true(T) or false(F)? (T/F): ').upper()
            if question_answer == 'T':
                true_or_false = True
            elif question_answer == 'F':
                true_or_false = False

            questions.append(Question(question_sentence, 'True or False', True, true_or_false))
            print(f'Question created! There are {len(questions)} questions now!')

        elif question_type == 'M':
            local_answers = []
            question_sentence = input('Enter the question: ')
            number_of_answers = int(input('Enter the number of options for this question: (2,3,4): '))
            right_answer = input('Enter the correct answer: ')
            local_answers.append([right_answer, True])
            for i in range(number_of_answers - 1):
                local_answers.append([input('Enter another option: '), False])

            questions.append(Question(question_sentence, 'Multiple Choice', False, local_answers))
            print(f'Question created! There are {len(questions)} questions now!')

        else:
            print('Invalid option!')

        print('###################################')
        print('###################################')
        print('\n')

        another = input('Do you want to create a question? (Y/N): ').upper()
        if another == 'Y':
            continue
        if another == 'N':
            break

    print('Question creation process completed!')
    print('###################################')
    print('###################################')

    return(questions)

def main():
    current_user = create_user()
    if current_user.creator:
        questions = create_questions()
    for question in questions:
        question.ask()
        question.answers(current_user)


main()