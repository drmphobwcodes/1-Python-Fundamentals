'''
Python Fundementals Workshop 5
Starter Template Version : 2.1
Author: Mpho Musengua
'''

# ---------- Task One ----------
# Guess the Number by User Input:
#     - Create a game where you have to guess a random number
#         within a certain range of integers.
#     - The game will always tell you whether your guess was too high or too low.
#     - Report to the User how many tries they have left and stop the game
#         when they have guessed the number or have no tries left.
#     - import the 'random' library to randomly pick a number


def guess_random_num(tries, start, stop):
    '''
    guess_random_num doc string
    '''


# ---------- Task Two  ----------
# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(n) - Linear Time


def guess_random_num_linear(tries, start, stop):
    '''
    guess_random_num_linear doc string
    '''

# ---------- Task Three ----------
# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(log(n)) - Logarithmic Time


def guess_random_num_binary(tries, start, stop):
    '''
    guess_random_num_binary doc string
    '''

# Add bonus task 1 - 3 here


def gambling_game():  # bonus task 4
    '''this is for bonus task 4 - make a game where you bet if the computer
    will win or not using the function from task two guess_random_num_linear(...).
    '''
    # set the return statements in guess_random_num_linear to return False or True

# Driver Code Task One
#   5 == tries
#   0, 10 == Range of random integers to choose from.


guess_random_num(5, 0, 10)

# Driver Code Task Two
#   5 == tries
#   0, 10 == Range of random integers to choose from.

guess_random_num_linear(5, 0, 10)

# Driver Code Task Three
#   5 == tries
#   0, 100 == Range of random integers to choose from.

guess_random_num_binary(5, 0, 100)


# Driver code for gambling game

# gambling_game()
