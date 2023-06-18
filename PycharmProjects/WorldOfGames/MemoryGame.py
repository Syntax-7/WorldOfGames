import time
import random
from Live import Person


class Guessing:
    generated_list = []
    user_guess = []


def generate_sequence():
    for i in range(Person.difficulty):
        Guessing.generated_list.append(random.randint(1, 101))
    return Guessing.generated_list


def list_pop():
    # Define the duration in seconds
    duration = 0.7
    # Generate and display the random number
    print(Guessing.generated_list, end=' ')
    # Add a delay of 0.7 seconds
    time.sleep(duration)
    # Print a new line after the sequence
    print()


def get_list_from_user():
    # Get input from the user
    input_string = input("Please enter the number you remember by order separated by spaces: ")

    # Split the input string into individual elements
    input_list = input_string.split()

    # Convert each element to an integer and adding it to the list
    Guessing.user_guess = [int(element) for element in input_list]


    return Guessing.user_guess


def is_list_equal():
    return Guessing.generated_list == Guessing.user_guess


def play():
    generate_sequence()
    list_pop()
    get_list_from_user()
    result = is_list_equal()
    print(result)


play()
