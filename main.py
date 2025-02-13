# Marisol Morales & Andreas Moreno, 2/13/24, State Capital Quiz Lab 3
import random
#import check_input, we end up not using this import as we create one within the function later on


def read_file(file_name):
  states_capital = []
  file = open(file_name)
  for line in file:
    pairs = line.strip().split(',')
    states_capital.append(pairs)
  file.close()
  return states_capital
  
def get_random_state(states):
  return random.choice(states)
  
def get_random_choices(states, correct_capital):
  choices = [correct_capital]
  for i in range(3):
    incorrect_capital = random.choice(states)[1]
    while incorrect_capital in choices:
      incorrect_capital = random.choice(states)[1]
    choices.append(incorrect_capital)
  random.shuffle(choices)
  return choices
   
      
def ask_question(correct_state, possible_answers):
  options = ['A', 'B', 'C', 'D']
  print('The capital of '+ correct_state + ' is: ')
  string_of_choices = ''
  for i, answer in enumerate(possible_answers):
    string_of_choices += (f' {options[i]}. {answer} ')
  print(string_of_choices)
  user_input = input('Enter selection: ').upper()  
  
  while user_input not in options:
    print('Invaild input. Input choice A-D.')
    user_input = input('Enter selection: ').upper()
  return options.index(user_input)

def main():
  states = read_file("statecapitals.txt")
  total_points = 0 
  num_of_questions = 1
  print('- State Capitals Quiz -')
  
  while num_of_questions < 11:
    correct_state, correct_capital = get_random_state(states)
    possible_answers = get_random_choices(states, correct_capital)
    print(f'{num_of_questions}.', end='')
    user_choice = ask_question(correct_state, possible_answers)
    
    if user_choice == possible_answers.index(correct_capital):
      total_points += 1
      print("Correct!")
    else: 
      print("Incorrect! The correct answer is {}.".format(correct_capital))
    
    num_of_questions += 1  
  print("End of test. You got {} correct.".format(total_points))

main()