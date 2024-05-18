# This a simple portofolio project to showcase python skills under the Codecademy lessons
# It's going to be a questionaire for friends, with a minimum of two players
# One or more friends write a personal questions quiz and the others have to guess the answer

import random
import json

# The user class defines the player data
class User:
    def __init__(self, username, creator = False):
        self.username = username
        self.creator = creator
        self.correct_answers = 0
        self.wrong_answers = 0
    def __repr__(self):
        return 'User'

# Question defines a question with its type. If TF options is a boolean if MCh then is a list.
class Question:
    def __init__(self, question, type_of_question, true_or_false = False, options = []):
        self.question = question
        self.type_of_question = type_of_question
        self.options = options
        self.true_or_false = true_or_false
    def __repr__(self):
        return 'Question'
    
    # .ask() prints each question
    def ask(self):
        print('\n')
        print('Question: ')
        print(self.question)
    
    # .answers() renders the answers and checks if the user input is correct or not
    # It prints the result and adds the record to the user
    def answers(self, user):
        if self.true_or_false:
            choice = input('Is it True or False?: (T/F): ').upper()
            if choice == 'T':
                choice = True
            elif choice == 'F':
                choice = False

            if choice == self.options:
                print('Correct!')
                print('\n')
                user.correct_answers += 1
            elif choice == self.options:
                print('Incorrect!')
                print('\n')
                user.wrong_answers += 1
        else:
            # randomly prints the options
            # correct_num keeps track of the num value that's associated with a True option.
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

# create_user() ask for the information to create an user object
def create_user():
    print('###################################')
    print('Welcome!')
    print('Let\'s start the program')
    username = input('Please provide your username: \n')
    creator = False
    role = input('Do you want to create questions(Q) or start answering(A)? (Q/A):').upper()
    if role == 'Q':
        creator = True
    return User(username, creator)

# create_questions() is a series of input steps to organize the question and return them as a list.
def create_questions():
    questions = []
    while True:
        print('\n')
        question_type = input('To create a Multiple Choice question enter M:\nTo create a True or False question enter T:\n').upper()

        if question_type == 'T':
            question_sentence = input('Enter the question: ')
            while True:
                question_answer = input('If the right answer is True enter T:\nIf the right answer is False enter F:\n').upper()
                if question_answer == 'T':
                    true_or_false = True
                    break
                elif question_answer == 'F':
                    true_or_false = False
                    break
                else:
                    print('Invalid input, try again!')

            questions.append(Question(question_sentence, 'True or False', True, true_or_false))
            print(f'Question created! There are {len(questions)} questions now!')

        elif question_type == 'M':
            local_answers = []
            question_sentence = input('Enter the question: ')
            number_of_answers = int(input('Enter the number of options for this question (2,3,4): '))
            right_answer = input('Enter the correct answer: ')
            local_answers.append([right_answer, True])
            for i in range(number_of_answers - 1):
                local_answers.append([input('Enter an incorrect option: '), False])

            questions.append(Question(question_sentence, 'Multiple Choice', False, local_answers))
            print(f'Question created! There are {len(questions)} questions now!')

        else:
            print('Invalid option!')

        print('###################################')
        print('\n')

        another = input('Do you want to create a question? (Y/N): ').upper()
        if another == 'Y':
            continue
        if another == 'N':
            break
    print('\n')
    print('Question creation process completed!')
    print('###################################')

    return(questions)

# save_questions() creates a dictionary, loops through the questions and save the info into a json file 
# the json file uses user.username as file name
def save_questions(questions_list, user):
    questions_dict = {}
    for i in range(len(questions_list)):
        questions_dict[i] = {
            'question': questions_list[i].question, 
            'type_of_question': questions_list[i].type_of_question, 
            'true_or_false': questions_list[i].true_or_false, 
            'options': questions_list[i].options
        }
    with open(f'{user.username.lower()}.json', 'w') as q_json:
        json.dump(questions_dict, q_json)
    print(f'Questions succesfully saved in {user.username}.json file.\nUse \'{user.username.lower()}\' to load them')

# use_saved_questions() tries to load a json file with the specified input string as a name
# then it creates a list of Question objects with the info.
def use_saved_questions():
    username = input('Please enter the username of the questions you want to answer: ').lower()
    with open(f'{username}.json', 'r') as q_json:
        questions_dict = json.load(q_json)
    questions_list = []
    for q in questions_dict.values():
        questions_list.append(Question(q['question'],q['type_of_question'],q['true_or_false'],q['options']))
    return questions_list

# main() runs the previous functions in order
def main():
    current_user = create_user()
    if current_user.creator:
        questions = create_questions()
        save_questions(questions, current_user)
    else:
        questions = use_saved_questions()
        for question in questions:
            question.ask()
            question.answers(current_user)
        print(f'Those were all the questions.\nYou ended up with {current_user.correct_answers} correct answers and {current_user.wrong_answers} wrong answers!')
        print('Good Bye!')

main()