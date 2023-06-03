from random import randint


class Guessing:
    secret_number = 1
    difficulty = 3


# Generates a random number fo the user to guess and saves in 'secret number' variable.
def generate_number():
    Guessing.secret_number = (randint(1, Guessing.difficulty))


# Compares results from the 'secret_number' variable & the output that returns from 'get_guess_from_user' function.
def compare_results():
    return Guessing.secret_number == get_guess_from_user()


# The function prompts the user to choose a number between 1 to the difficulty number & returns a value for the
# 'compare_results' function to handle.
def get_guess_from_user():
    user_input = int(input(f"Please guess a number between 1 to {Guessing.difficulty}: "))
    while not user_input in range(1, Guessing.difficulty + 1):
        user_input = int(
            input(f"You have picked {user_input}. Please guess a number between 1 to {Guessing.difficulty}: "))
    return user_input


# Calls the 'generate_number', 'compare_results' functions & prints the boolean that returns from 'compare results'
# function : True=Win\False=Lost.
def play():
    generate_number()
    result = compare_results()
    print(result)


play()
