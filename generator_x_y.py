import random
from random import randrange


class GeneratorXY:
    """Generator random x and y for our object"""

    @staticmethod
    def generate_new_coord(cell):

        # если рыбка не возле стенок
        if 0 < cell.x < cell.settings.num_cols - 1 and 0 < cell.y < cell.settings.num_rows - 1:
            new_x = random.choice((cell.x - 1, cell.x + 1))
            new_y = random.choice((cell.y - 1, cell.y + 1))

        # если рыбка возле левого края
        elif cell.x == 0 and cell.y != 0 and cell.y != cell.settings.num_rows - 1:
            new_x = cell.x + 1
            new_y = random.choice((cell.y - 1, cell.y + 1))

        # рыбка возле верхнего края
        elif cell.y == 0 and cell.x != 0 and cell.x < cell.settings.num_cols - 1:
            new_x = random.choice((cell.x - 1, cell.x + 1))
            new_y = cell.y + 1

        # рыбка возле правого края
        elif cell.y != 0 and cell.y != cell.settings.num_rows - 1 and cell.x == cell.settings.num_cols - 1:
            new_x = cell.x - 1
            new_y = random.choice((cell.y - 1, cell.y + 1))

        # рыбка возле нижнего края
        elif cell.y == cell.settings.num_rows - 1 and cell.x != 0 and cell.x < cell.settings.num_cols - 1:
            new_y = cell.y - 1
            new_x = random.choice((cell.x - 1, cell.x + 1))

        # рыбка в верхнем левом углу
        elif cell.x == 0 and cell.y == 0:
            new_x = cell.x + 1
            new_y = cell.y + 1
        # рыбка в нижнем левом углу
        elif cell.x == 0 and cell.y == cell.settings.num_rows - 1:
            new_x = random.choice((cell.x + 1, cell.x))
            new_y = random.choice((cell.y - 1, cell.y))
        # рыбка в нижнем правом углу
        elif cell.x == cell.settings.num_cols - 1 and cell.y == cell.settings.num_rows - 1:
            new_x = random.choice((cell.x - 1, cell.x))
            new_y = random.choice((cell.y - 1, cell.y))
        # рыбка в верхнем правом углу
        elif cell.x == cell.settings.num_cols - 1 and cell.y == 0:
            new_x = cell.x - 1
            new_y = cell.y + 1
        else:
            new_x = randrange(cell.x - 1, cell.x + 1)
            new_y = randrange(cell.y - 1, cell.y + 1)
        # переделать без проверок
        # for i in range(4):
        if new_x == cell.x and new_y == cell.y:
            GeneratorXY.generate_new_coord(cell)

        return new_x, new_y
