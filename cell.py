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
        self.time_to_reproduce = settings.time_to_reproduce


    def __repr__(self):
        return

    def __move_in_free_cell(self):
        new_x, new_y = self.__get_empty_neighbor_coord()
        if self.ocean.cells[new_y][new_x] is None:
            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[new_y][new_x] = self

            self.time_to_reproduce -= 1

    def __get_empty_neighbor_coord(self):
        new_x = -1
        new_y = -1
        while new_x < 0 or new_y < 0:
            new_x, new_y = self.__generate_new_coord()

        return new_x, new_y

    def __generate_new_coord(self):

        new_x = randrange(self.x - 1, self.x + 1)
        new_y = randrange(self.y - 1, self.y + 1)
        # переделать без проверок
        if new_x == self.x and new_y == self.y:
            self.__generate_new_coord()

        return new_x, new_y


    def process(self):
        """Перемещает в соседнюю ячейку, используя определенные правила (в зависимости от подкласса)"""
        self.__move_in_free_cell()

    def get_prey_neighbor_coord(self, Prey):
        all_neighbors = [self.west(), self.north(), self.south(), self.east(),]
        preys = []

        for neighbor in all_neighbors:
            if type(neighbor) == Prey:
                preys.append(neighbor)

                print(f'neighbors = {neighbor.x},{neighbor.y}')   ####
        # print(preys)
        if preys:
            prey = random.choice(preys)
            print(f'choise prey - {prey.x, prey.y}')        #######
            # eat prey, занять новое место
            # print(self.ocean.cells[prey.y][prey.x])


            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[prey.y][prey.x] = self
            self.x = prey.x
            self.y = prey.y

            self.ocean.cells[prey.y][prey.x].is_hungry = False
            # чтобы predator, когда тот ест рыбку справа или снизу, снова не вызывал метод process,
            # для фикса этого бага применяю флаг is_hungry, который сообщает о том, что predator на этой итерации уже ел,
            # кормим рыбку, теперь она не голодная
            self.is_hungry = False
            # self.ocean.display_cells(self.settings)       ########
            # освободить место
            # self.ocean.cells[self.y][self.x] = None

    def set_predator_is_hungry(self, Predator):
        for y in range(self.ocean.num_rows):
            for x in range(self.ocean.num_cols):
                if type(self.ocean.cells[y][x]) == Predator:
                    self.ocean.cells[y][x].is_hungry = True
                    # print(self.ocean.cells[y][x])
                    # print(self.ocean.cells[y][x].is_hungry)

    # def find_prey_from_neighbors(self, Prey):
    #
    #     status = False
    #     prey = None
    #
    #     all_neighbors = [self.west(), self.north()]#, self.south(), self.east(),]
    #     print(all_neighbors)    ##################3
    #
    #     preys = []
    #     for neighbor in all_neighbors:
    #         if type(neighbor) == Prey:
    #             preys.append(neighbor)
    #
    #     if preys:
    #         prey = random.choice(preys)
    #         print(prey.x, prey.y)
    #
    #     if prey:
    #         # eat prey, занять новое место
    #         self.ocean.cells[prey.y][prey.x] = self
    #         # освободить место
    #         self.ocean.cells[self.y][self.x] = None
    #
    #
    #         self.time_to_feed = self.settings.time_to_feed
    #         status = True
    #         self.flag = True
    #         # print(self.x, self.y)
    #
    #     return status
    #
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