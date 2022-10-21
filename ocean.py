from random import randint
from prey import Prey
from predator import Predator
from obstacle import Obstacle
from ui import *

class Ocean:
    """Ocean is a 2D cell array. The ocean has prey, predators, obstacles and empty cell"""
    cells = []

    def __init__(self, settings):
        self.settings = settings
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.prey_number = settings.prey_number
        self.predators_number = settings.predators_number
        self.obstacles_number = settings.obstacles_number
        self.prey = Prey(self, self.settings, 0, 0)
        self.predator = Predator(self, self.settings, 0, 0)
        self.obstacle = Obstacle(self, self.settings, 0, 0)

    def __create_ocean(self):
        """Fill ocean with cells"""
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                self.cells[y].append(None)

    def __add_inhabitants(self):
        """Add inhabitants of ocean: obstacles, prey, predator"""
        inhabitants = {Obstacle: self.obstacle,
                       Prey: self.prey,
                       Predator: self.predator}

        for key, value in inhabitants.items():
            self.__add_element(value, key)

    def __add_element(self, ocean_element, ocean_elements_type):
        """Add inhabitant to ocean in free cells"""
        i = 0
        while i != ocean_element.number_of_element:
            x = randint(0, self.num_cols - 1)
            y = randint(0, self.num_rows - 1)
            if self.cells[y][x] is None:
                self.cells[y][x] = ocean_elements_type(self, self.settings, x, y)
            else:
                continue
            i += 1

    def display_cells(self):
        """Print all cells"""
        print('\t', end='')
        print('\033[34m⥎\033[0m\t' * self.num_cols)
        for x in range(self.num_rows):
            print('\033[34m⥑\033[0m\t', end='')

            for y in range(len(self.cells[x])):
                if self.cells[x][y]:
                    print(f'{self.cells[x][y]}\t', end='')
                else:
                    print(f'{self.settings.image_for_cell}\t', end='')
            print('\033[34m⥏\033[0m\t', end='')
            print()
        print('\t', end='')
        print('\033[34m⥐\033[0m\t' * self.num_cols)

    def display_stats(self):
        """Обновляет отображаемый номер итерации, количество преград, хищников и добычи"""
        preys = []
        obstacles = []
        predators = []
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == Prey:
                    preys.append(self.cells[x][y])
                if type(self.cells[x][y]) == Predator:
                    predators.append(self.cells[x][y])
                if type(self.cells[x][y]) == Obstacle:
                    obstacles.append(self.cells[x][y])

        return print(f'preys = {len(preys)}, predators = {len(predators)}, obstacles = {len(obstacles)}')

    def __process(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if type(self.cells[y][x]) == Prey or type(self.cells[y][x]) == Predator:
                    if self.cells[y][x].is_hungry:
                        self.cells[y][x].process()
        self.predator.set_predator_is_hungry()
        self.display_cells()

    def get_coord_for_all_prey(self):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == Prey:
                    print(f'{self.cells[x][y]} x = {self.cells[x][y].x}, y = {self.cells[x][y].y}')

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        # number_iteration = get_number_iteration()
        number_iteration = 50
        self.__create_ocean()
        self.__add_inhabitants()
        self.display_stats()
        self.display_cells()

        for i in range(number_iteration):
            print()
            self.__process()

        self.display_stats()

    def initialize(self):
        """init prey, predator, obstacle"""
        pass
