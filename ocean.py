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
        self.number_iteration = settings.number_iteration
        self.prey_ = Prey  # (self, self.settings, 0, 0)
        self.predator_ = Predator  #(self, self.settings, 0, 0)
        self.obstacle_ = Obstacle  #(self, self.settings, 0, 0)

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

    def display_screen(self):
        """Print all cells"""
        UI.print_border(self)
        UI.show_cells(self)

    def display_stats(self, i):
        UI.display_stats(self, i)

    def __process(self):
        """Аor each cell, if is not None, and if is a predator or prey, and is not hungry (not eat in this iteration),
        execute the process,
        set for all predator is_hungry, already_moving"""

        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if self.cells[y][x] is not None and type(self.cells[y][x]) is not Obstacle and \
                        not self.cells[y][x].already_moving and self.cells[y][x].is_hungry:
                    self.cells[y][x].process()
        self.predator.set_predator_is_hungry()
        self.predator.set_already_moving()

    def run(self):
        """Starts modeling"""
        number_iteration = self.settings.number_iteration
        self.__create_ocean()
        self.__add_inhabitants()
        self.display_screen()
        # self.display_stats(0)
        max_iteration = 0
        for i in range(number_iteration):
            self.__process()
            # self.display_screen()
            # self.display_stats(i)
            if self.prey_number == 0 or self.predators_number == 0:
                UI.finish_simulation(self, i)
                break
            max_iteration += 1

        self.display_screen()

        print(f'max_iteration = {max_iteration}')
        self.display_stats(max_iteration)
