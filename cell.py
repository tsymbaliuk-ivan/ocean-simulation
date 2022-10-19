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




    # def find_neighbors(self):
    #     all_neighbor = [self.east()]
    #     print(all_neighbor)
    #
    #
    # def find_prey(self, predator, Prey):
    #     """Ищет соседнюю ячейку с добычей"""
    #
    #     east_neighbor = self.east()
    #
    #     if type(east_neighbor) == Prey:
    #         self.ocean.cells[self.y][self.x + 1] = self
    #         self.ocean.cells[self.y][self.x] = None
    #         return True
    #     else:
    #         return False
    #
    # def east(self):
    #     """Возвращает ячейку, на востоке от данной"""
    #     if self.x + 1 < self.ocean.num_cols:
    #         # print(self.ocean.cells[self.y][self.x])
    #         # print(self.x, self.y)
    #         return self.ocean.cells[self.y][self.x]



    def get_cell_at(self, a_coord):
        """Возвращает ячейку с координатами a_coord в массиве cells из ocean"""
        pass

    def assign_cell_at(self, a_coord, a_cell):
        """Помещает ячейку a_cell в место с координатоми a_coord в массиве cells"""
        pass

    def north(self):
        """Возвращает ячейку, на севере от данной"""
        pass

    def south(self):
        """Возвращает ячейку, на юге от данной"""
        pass

    def west(self):
        """Возвращает ячейку, на западе от данной"""
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