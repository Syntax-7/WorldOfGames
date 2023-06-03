from MemoryGame import play
class Person:
    name = 0
    game_num = 0
    difficulty = 0


# The player inputs his name
def welcome():
    Person.name = input("Greetings player please enter your name: ")
    print(f'Hello {Person.name} and welcome to the World of Games (WoG).\n Here you can find many cool games to play.')


# The player inputs the game choice within the restriction of 3 options & the difficulty within 5.
def load_game():
    while not int(Person.game_num) in range(1, 4):
        Person.game_num = input('Please choose a game to play:\n'
                                '1. Memory Game - a sequence of numbers will appear for 1 second and you have to '
                                'guess it back.\n'
                                '2. Guess Game - guess a number and see if you chose like the computer.\n'
                                '3. Currency Roulette - try and guess the value of a random amount of USD in ILS.')

    while not int(Person.difficulty) in range(1, 6):
        Person.difficulty = input('Please choose game difficulty from 1 to 5:')

if(Person.game_num= 1)
    play(Person.difficulty)