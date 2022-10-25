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
        self.prey = Prey(self, self.settings, 0, 0)
        self.predator = Predator(self, self.settings, 0, 0)
        self.obstacle = Obstacle(self, self.settings, 0, 0)

    def __create_ocean(self):
        """Fill ocean with cells"""
        for y in range(self.settings.num_rows):
            self.cells.append([])
            for x in range(self.settings.num_cols):
                self.cells[y].append(None)

    def __add_inhabitants(self):
        """Add inhabitants of ocean: obstacles, prey, predator"""
        inhabitants = {Obstacle: self.obstacle,
                       Prey: self.prey,
                       Predator: self.predator}

        for key, value in inhabitants.items():
            self.__add_element(key, value)

    def __add_element(self, ocean_elements_type, ocean_element):
        """Add inhabitant to ocean in free cells"""
        i = 0
        while i != ocean_element.number_of_element:
            x = randint(0, self.settings.num_cols - 1)
            y = randint(0, self.settings.num_rows - 1)
            if self.cells[y][x] is None:
                self.cells[y][x] = ocean_elements_type(self, self.settings, x, y)
            else:
                continue
            i += 1

    def find_neighbors(self, cell) -> list:
        """Find nearest neighbors if exist"""
        all_neighbors = [self.west(cell), self.north(cell), self.south(cell), self.east(cell)]
        return all_neighbors

    def east(self, cell):
        """Returns the cell east of the given one, if any."""
        if cell.x + 1 < self.settings.num_cols:
            return self.cells[cell.y][cell.x + 1]

    def north(self, cell):
        """Returns the cell north of the given"""
        if cell.y - 1 >= 0:
            return self.cells[cell.y - 1][cell.x]

    def south(self, cell):
        """Returns the cell south of the given"""
        if cell.y + 1 < self.settings.num_rows:
            return self.cells[cell.y + 1][cell.x]

    def west(self, cell):
        """Returns the cell west of the given"""
        if cell.x - 1 >= 0:
            return self.cells[cell.y][cell.x - 1]

    def try_to_reproduce_fish(self, fish, old_x, old_y):
        """Reproduce yourself to the cell with coordinates old_x, old_y in the cells array"""
        if fish.time_to_reproduce <= 0 and self.cells[old_y][old_x] is None:
            if isinstance(fish, Prey):
                self.cells[old_y][old_x] = Prey(self, self.settings, old_x, old_y)
                self.settings.prey_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_prey

            elif isinstance(fish, Predator):
                self.cells[old_y][old_x] = Predator(self, self.settings, old_x, old_y)
                self.settings.predators_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_predator

    def __process(self):
        """Аor each cell, if is not None, and if is a predator or prey, and is not hungry (not eat in this iteration),
        execute the process,
        set for all predator is_hungry, already_moving"""

        for y in range(self.settings.num_rows):
            for x in range(self.settings.num_cols):
                if self.cells[y][x] is not None and type(self.cells[y][x]) is not Obstacle and \
                        not self.cells[y][x].already_moving and self.cells[y][x].is_hungry:
                    self.cells[y][x].process()
        self.predator.set_predator_is_hungry()
        self.set_already_moving()

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
            if self.settings.prey_number == 0 or self.settings.predators_number == 0:
                UI.finish_simulation(self, i)
                break
            max_iteration += 1

        self.display_screen()

        print(f'max_iteration = {max_iteration}')
        self.display_stats(max_iteration)

    def display_screen(self):
        """Print all cells"""
        UI.print_border(self)
        UI.show_cells(self)

    def display_stats(self, i):
        UI.display_stats(self, i)

    def set_already_moving(self):
        """Set all predator  already_moving - False"""
        for y in range(self.settings.num_rows):
            for x in range(self.settings.num_cols):
                if isinstance(self.cells[y][x], type(self.prey)) or isinstance(self.cells[y][x], type(self.predator)):
                    self.cells[y][x].already_moving = False
