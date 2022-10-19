import random

from coordinate import Coordinate
from random import randint, randrange
# from prey import Prey
# from predator import Predator

class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""
    def __init__(self, ocean, settings, x, y):
        self.ocean = ocean
        self.x = x
        self.y = y
        self.settings = settings


    def __repr__(self):
        return

    def move_in_free_cell(self):
        new_x, new_y = self.get_empty_neighbor_coord()
        if self.ocean.cells[new_y][new_x] is None:
            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[new_y][new_x] = self

    def get_empty_neighbor_coord(self):
        new_x = -1
        new_y = -1
        while new_x < 0 or new_y < 0:
            new_x, new_y = self.generate_new_coord()

        return new_x, new_y

    def generate_new_coord(self):

        new_x = randrange(self.x - 1, self.x + 1)
        new_y = randrange(self.y - 1, self.y + 1)
        # переделать без проверок
        if new_x == self.x and new_y == self.y:
            self.generate_new_coord()

        return new_x, new_y


    def process(self):
        """Перемещает в соседнюю ячейку, используя определенные правила (в зависимости от подкласса)"""
        self.move_in_free_cell()


    def find_prey_from_neighbors(self, Prey, settings):

        status = False
        prey = None
        all_neighbors = [self.east(), self.west(), self.north(), self.south()]
        print(all_neighbors)
        preys = []
        for neighbor in all_neighbors:
            if type(neighbor) == Prey:
                preys.append(neighbor)

        if preys:
            prey = random.choice(preys)
            print(prey.x, prey.y)

        if prey:
            # eat prey
            self.ocean.cells[prey.y][prey.x] = self
            self.ocean.cells[self.y][self.x] = None
            self.ocean.display_cells(settings)
            self.time_to_feed = settings.time_to_feed
            status = True

        return status

    def east(self):
        """Возвращает ячейку, на востоке от данной, если она есть"""
        if self.x + 1 < self.ocean.num_cols:
            return self.ocean.cells[self.y][self.x + 1]

    def north(self):
        """Возвращает ячейку, на севере от данной"""
        if self.y - 1 >= 0:
            return self.ocean.cells[self.y - 1][self.x]

    def south(self):
        """Возвращает ячейку, на юге от данной"""
        if self.y + 1 < self.ocean.num_rows:
            return self.ocean.cells[self.y + 1][self.x]

    def west(self):
        """Возвращает ячейку, на западе от данной"""
        if self.x - 1 >= 0:
            return self.ocean.cells[self.y][self.x - 1]

    def get_cell_at(self, a_coord):
        """Возвращает ячейку с координатами a_coord в массиве cells из ocean"""
        pass

    def assign_cell_at(self, a_coord, a_cell):
        """Помещает ячейку a_cell в место с координатоми a_coord в массиве cells"""
        pass

    def get_off_set(self):
        """Возвращает смещение"""
        pass

    def set_off_set(self, a_coord):
        """Устанавливает смещение в a_coord"""
        pass

    def get_image(self):
        """return image"""
        pass

    def display(self):
        """Выводит изображение по соответствующему смещению"""
        pass