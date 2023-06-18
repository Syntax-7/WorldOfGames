class Person:
    name = ""
    game_num = 0
    difficulty = 0


# The player inputs his name
def welcome():
    Person.name = input("Greetings player please enter your name: ")
    print(f'Hello {Person.name} and welcome to the World of Games (WoG).'
          f'\nHere you can find many cool games to play.')


# The player inputs the game choice within the restriction of 3 options & the difficulty within 5.
def load_game():
    while int(Person.game_num) not in range(1, 4):
        print('Please choose a game to play:\n'
              '1. Memory Game - a sequence of numbers will appear for 1 second and you have to '
              'guess it back.\n'
              '2. Guess Game - guess a number and see if you chose like the computer.\n'
              '3. Currency Roulette - try and guess the value of a random amount of USD in ILS.')

        Person.game_num = int(input('Please choose a game number (1-3):'))

    while int(Person.difficulty) not in range(1, 6):
        Person.difficulty = int(input('Please choose game difficulty from 1 to 5:'))

    print("Starting the game, Get ready..")

    if Person.game_num == 1:
        import MemoryGame
    elif Person.game_num == 2:
        import GuessGame
    else:
        import CurrencyRouletteGame
