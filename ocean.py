from random import randint
from prey import Prey
from predator import Predator
from obstacle import Obstacle
from ui import UI

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
        UI.show_cells(self)

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

        UI.display_stats(preys, predators, obstacles)

    def __process(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if self.cells[y][x] is not None and type(self.cells[y][x]) is not Obstacle and \
                        not self.cells[y][x].already_moving and self.cells[y][x].is_hungry:
                    self.cells[y][x].process()
        self.predator.set_predator_is_hungry()
        self.predator.set_alredy_moving()
        self.display_cells()


    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        # number_iteration = UI.get_number_iteration()
        number_iteration = 30
        self.__create_ocean()
        self.__add_inhabitants()
        self.display_stats()
        self.display_cells()

        for i in range(number_iteration):
            UI.print_border(self)
            self.__process()

        self.display_stats()

    def initialize(self):
        """init prey, predator, obstacle"""
        pass
