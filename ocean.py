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

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        pass

    def process(self):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if self.cells[x][y]:
                    self.cells[x][y].process()



    def get_number_preys(self):
        preys = []
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == Prey:
                    preys.append(self.cells[x][y])
        return preys

    # def process(self, prey, settings):
    #
    #     preys = self.get_all_preys(prey)
    #     print(preys)
    #
    #     for prey in preys:
    #         if prey.time_to_reproduce == 0:
    #             self.cells[prey.x][prey.y] = Cell(settings, prey.x, prey.y)
    #         else:
    #             new_x = randrange(prey.x - 1, prey.x + 1)
    #             new_y = randrange(prey.y - 1, prey.y + 1)
    #             self.cells[new_x][new_y] = Prey(settings, new_x, new_y)
    #             self.cells[new_x][new_y].time_to_reproduce -= 1
    #
    #     # if prey.time_to_reproduce == 0:
    #     #     self.cells[x][y] = Cell(settings, x, y)
    #     # else:
    #     #     self.cells[x][y] = Cell(settings, x, y)
    #     #     new_x = randrange(x - 1, x + 1)
    #     #     new_y = randrange(y - 1, y + 1)
    #     #     self.cells[new_x][new_y] = Prey(settings, new_x, new_y)
    #     #     prey.time_to_reproduce -= 1

    def get_coord_for_all_prey(self, prey):
        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                if type(self.cells[x][y]) == Prey:
                    print(f'{self.cells[x][y]} x = {self.cells[x][y].x}, y = {self.cells[x][y].y}')
