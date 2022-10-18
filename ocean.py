from random import randint, randrange
from cell import Cell
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

    def add_inhabitants(self, obstacles, prey, predator, settings):
        """Add inhabitants of ocean: obstacles, prey, predator"""
        ocean_elements = obstacles, prey, predator
        ocean_elements_type = Obstacle, Prey, Predator

        for i in range(len(ocean_elements)):
            self.add_element(ocean_elements[i], settings, ocean_elements_type[i])

        # for ocean_element in ocean_elements:
        #     self.add_element(ocean_element, settings, ocean_elements_type[i])

    def add_element(self, ocean_element, settings, ocean_elements_type):
        """Add inhabitant to ocean in free cells"""
        i = 0
        while i != ocean_element.number_of_element:
            x = randint(0, self.num_cols - 1)
            y = randint(0, self.num_rows - 1)
            if type(self.cells[y][x]) == type(Cell(settings)):  # use isinstance
                self.cells[y][x] = ocean_elements_type(settings, x, y)
                # self.cells[y][x] = ocean_element
            else:
                continue
            i += 1

    def add_preys(self, prey, settings):
        """Add inhabitant to ocean in free cells"""
        i = 0
        while i != prey.number_of_element:
            x = randint(0, self.num_cols - 1)
            y = randint(0, self.num_rows - 1)
            if type(self.cells[y][x]) == type(Cell(settings)):  # use isinstance
                # self.cells[y][x] = Prey(settings, x, y)
                self.cells[y][x] = Prey(settings, x, y)
            else:
                continue
            i += 1

    def get_num_prey(self):
        """return number of prey"""
        pass

    def set_num_prey(self, a_number):
        """set number of prey"""
        self.prey_number = a_number

    def get_num_predators(self):
        """return number of predators"""

        return self.predators_number

    def initialize(self):
        """init size ocean, prey, predator, obstacle"""
        pass

    def init_cells(self, obstacles_number, prey_number, predators_number):
        self.prey_number = prey_number
        self.predators_number = predators_number
        self.obstacles_number = obstacles_number

    def add_predators(self, num_predators):
        self.predators_number = num_predators

    def add_prey(self, num_prey):
        self.prey_number = num_prey

    def display_border(self):
        """отображает максимальную ограниченную область океана (горизонтальная граница)"""
        pass

    def display_cells(self):
        """пересчитывает и выводит массив cells"""

        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                print(f'{self.cells[x][y]}\t', end='')
            print()
        # print(self.cells[1][4].x)
        # print(self.cells[1][4].y)

    def display_stats(self):
        """Обновляет отображаемый номер итерации, количество преград, хищников и добычи"""
        pass

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        pass

    def create_ocean(self, settings):
        # заполним все места пробелами
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                self.cells[y].append(Cell(settings, x, y))

    def process(self, prey, cell):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == type(prey):

                    if prey.time_to_reproduce == 0:
                        self.cells[x][y] = cell
                    else:
                        new_x = randrange(x - 1, x + 1)
                        new_y = randrange(y - 1, y + 1)
                        prey.time_to_reproduce -= 1
                        self.cells[new_x][new_y] = prey

    def get_coord_for_all_prey(self, prey):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == type(prey):
                    print(f'{self.cells[x][y]} x = {self.cells[x][y].x}, y = {self.cells[x][y].y}')
