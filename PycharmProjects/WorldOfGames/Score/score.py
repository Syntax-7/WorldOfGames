POINTS_OF_WINNING = 0
from Live import Person


def add_score():
    try:
        with open("scores.txt", "r+") as file:
            current_score = int(file.read())
            points = (Person.difficulty * 3) + 5
            new_score = current_score + points
            file.seek(0)
            file.write(str(new_score))
            file.truncate()
    except FileNotFoundError:
        with open("scores.txt", "w") as file:
            points = (Person.difficulty * 3) + 5
            file.write(str(points))
