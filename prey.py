from cell import Cell
from random import randint, randrange


class Prey(Cell):
    """Subclass Cell, prey. Can move, breed and be eaten"""

    def __init__(self, ocean, settings, x=0, y=0):
        super().__init__(ocean, x, y)
        self.settings = settings
        self.ocean = ocean
        self.image = settings.image_for_prey
        self.time_to_reproduce = 6
        self.number_of_element = settings.prey_number
        self.x = x
        self.y = y


    def __repr__(self):
        return self.settings.image_for_prey

    def process(self):
        """Перемещается, если возможно в пустую ячейку и уменьшает time_to_reproduce на 1"""


        print(f'before process for prey {self.x, self.y}')

        # print(self.ocean.cells[self.y][self.x])

        print(f'find new cell {self.find_cell()}')
        new_x, new_y = self.find_cell()
        print(f'is vacant {self.is_vacant_cell(new_x, new_y)}')

    def find_cell(self):
        new_x = -1
        new_y = -1
        while new_x < 0 or new_y < 0:
            new_x, new_y = self.generate_new_coord()

        return new_x, new_y

    def generate_new_coord(self):
        new_x = randrange(self.x - 1, self.x + 1)
        new_y = randrange(self.y - 1, self.y + 1)

        return new_x, new_y

    def is_vacant_cell(self, new_x, new_y):

        print(f'what inside {type(self.ocean.cells[new_x][new_y])}')
        if self.ocean.cells[new_x][new_y] is None:
            return True
        else:
            return False







    def move_from(self, from_coord, to_coord):
        """Перемещает из координаты from_coord, в координаты to_coord в массиве cells"""
        pass

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass
