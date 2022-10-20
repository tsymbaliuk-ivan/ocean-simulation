from random import randint
from prey import Prey
from predator import Predator
from obstacle import Obstacle


class Ocean:
    """Ocean is a 2D cell array. The ocean has prey, predators, obstacles and empty cell"""
    cells = []

    def __init__(self, settings):
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.prey_number = settings.prey_number
        self.predators_number = settings.predators_number
        self.obstacles_number = settings.obstacles_number

    def create_ocean(self):
        """Fill ocean with cells"""
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                self.cells[y].append(None)

    def add_inhabitants(self, obstacles, prey, predator, settings):
        """Add inhabitants of ocean: obstacles, prey, predator"""
        ocean_elements = obstacles, prey, predator
        ocean_elements_type = Obstacle, Prey, Predator

        for i in range(len(ocean_elements)):
            self.add_element(ocean_elements[i], settings, ocean_elements_type[i])

    def add_element(self, ocean_element, settings, ocean_elements_type):
        """Add inhabitant to ocean in free cells"""
        i = 0
        while i != ocean_element.number_of_element:
            x = randint(0, self.num_cols - 1)
            y = randint(0, self.num_rows - 1)
            if self.cells[y][x] is None:
                self.cells[y][x] = ocean_elements_type(self, settings, x, y)
            else:
                continue
            i += 1

    def display_cells(self, settings):
        """Print all cells"""
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if self.cells[x][y]:
                    print(f'{self.cells[x][y]}\t', end='')
                else:
                    print(f'{settings.image_for_cell}\t', end='')
            print()

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

    def process(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if type(self.cells[y][x]) == Prey or type(self.cells[y][x]) == Predator:
                    if self.cells[y][x].is_hungry:
                        self.cells[y][x].process()

    def get_coord_for_all_prey(self):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == Prey:
                    print(f'{self.cells[x][y]} x = {self.cells[x][y].x}, y = {self.cells[x][y].y}')

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        pass

    def initialize(self):
        """init size ocean, prey, predator, obstacle"""
        pass
