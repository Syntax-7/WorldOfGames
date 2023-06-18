SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1
import os


def Screen_cleaner():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')
