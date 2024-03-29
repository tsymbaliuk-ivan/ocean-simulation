from random import randint
from prey import Prey
from predator import Predator
from obstacle import Obstacle
from plankton import Plankton
from ui import UI


class Ocean:
    """Ocean is a 2D cell array. The ocean has prey, predators, obstacles and empty cell"""
    cells = []

    def __init__(self, settings):
        self.settings = settings
        self.prey = Prey(self, self.settings, 0, 0)
        self.predator = Predator(self, self.settings, 0, 0)
        self.obstacle = Obstacle(self, self.settings, 0, 0)
        self.plankton = Plankton(self, self.settings, 0, 0)
        self.iteration = 0

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
                       Predator: self.predator,
                       Plankton: self.plankton}

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
        all_neighbors = [self.__west(cell), self.__north(cell), self.__north_east(cell), self.__north_west(cell),
                         self.__south(cell), self.__south_east(cell), self.__east(cell), self.__south_west(cell)]
        return all_neighbors

    def __south_west(self, cell):
        """Returns the cell south_west of the given one."""
        if cell.x - 1 >= 0 and cell.y + 1 < self.settings.num_rows:
            if self.cells[cell.y + 1][cell.x - 1] is None:
                # coord = Coordinate(cell.x - 1, cell.y + 1)
                x = cell.x - 1
                y = cell.y + 1
                return x, y
            return self.cells[cell.y + 1][cell.x - 1]

    def __north_west(self, cell):
        """Returns the cell north_west of the given one."""
        if cell.x - 1 >= 0 and cell.y - 1 >= 0:
            if self.cells[cell.y - 1][cell.x - 1] is None:
                x = cell.x - 1
                y = cell.y - 1
                return x, y
            return self.cells[cell.y - 1][cell.x - 1]

    def __north_east(self, cell):
        """Returns the cell north_east of the given one."""
        if cell.x + 1 < self.settings.num_cols and cell.y - 1 >= 0:
            if self.cells[cell.y - 1][cell.x + 1] is None:
                x = cell.x + 1
                y = cell.y - 1
                return x, y
            return self.cells[cell.y - 1][cell.x + 1]

    def __south_east(self, cell):
        """Returns the cell south_east of the given one."""
        if cell.x + 1 < self.settings.num_cols and cell.y + 1 < self.settings.num_rows:
            if self.cells[cell.y + 1][cell.x + 1] is None:
                x = cell.x + 1
                y = cell.y + 1
                return x, y
            return self.cells[cell.y + 1][cell.x + 1]

    def __east(self, cell):
        """Returns the cell east of the given one, if any."""
        if cell.x + 1 < self.settings.num_cols:
            if self.cells[cell.y][cell.x + 1] is None:
                x = cell.x + 1
                y = cell.y
                return x, y
            return self.cells[cell.y][cell.x + 1]

    def __north(self, cell):
        """Returns the cell north of the given"""
        if cell.y - 1 >= 0:
            if self.cells[cell.y - 1][cell.x] is None:
                x = cell.x
                y = cell.y - 1
                return x, y
            return self.cells[cell.y - 1][cell.x]

    def __south(self, cell):
        """Returns the cell south of the given"""
        if cell.y + 1 < self.settings.num_rows:
            if self.cells[cell.y + 1][cell.x] is None:
                x = cell.x
                y = cell.y + 1
                return x, y
            return self.cells[cell.y + 1][cell.x]

    def __west(self, cell):
        """Returns the cell west of the given"""
        if cell.x - 1 >= 0:
            if self.cells[cell.y][cell.x - 1] is None:
                x = cell.x - 1
                y = cell.y
                return x, y
            return self.cells[cell.y][cell.x - 1]

    def try_to_reproduce_fish(self, fish, x, y):
        """Reproduce yourself to the cell with coordinates old_x, old_y in the cells array"""
        if fish.time_to_reproduce <= 0 and (self.cells[y][x] is None or type(self.cells[y][x]) == Plankton):
            if isinstance(fish, Prey):
                self.cells[y][x] = Prey(self, self.settings, x, y)
                self.settings.prey_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_prey

            elif isinstance(fish, Predator):
                self.cells[y][x] = Predator(self, self.settings, x, y)
                self.settings.predators_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_predator

            elif isinstance(fish, Plankton):
                self.cells[y][x] = Plankton(self, self.settings, x, y)
                self.settings.plankton_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_plankton

    def __process(self):
        """Аor each cell, if is not None, and if is a predator or prey, and is not hungry (not eat in this iteration),
        execute the process,
        set for all predator is_hungry, already_moving"""

        for y in range(self.settings.num_rows):
            for x in range(self.settings.num_cols):
                if (type(self.cells[y][x]) is Prey or type(self.cells[y][x]) is Predator
                        or type(self.cells[y][x]) is Plankton) and not self.cells[y][x].moved:
                    self.cells[y][x].process()
        self.set_moved_to_false()

    def run(self):
        """Starts modeling"""
        number_iteration = self.settings.number_iteration
        self.__create_ocean()
        self.__add_inhabitants()
        self.__display_screen()
        self.__display_stats(self.iteration)
        for i in range(number_iteration):
            self.__process()
            self.add_plankton()
            self.__display_screen()
            self.__display_stats(i)
            if self.settings.prey_number == 0 or self.settings.predators_number == 0:
                UI.finish_simulation(self, i)
                break
            self.iteration += 1

        self.__display_screen()
        self.__display_stats(self.iteration)

    def __display_screen(self):
        """Print all cells"""
        UI.print_border(self)
        UI.show_cells(self)

    def __display_stats(self, i):
        UI.display_stats(self, i)

    def set_moved_to_false(self):
        """Set all predator  already_moving - False"""
        for y in range(self.settings.num_rows):
            for x in range(self.settings.num_cols):
                if isinstance(self.cells[y][x], type(self.prey)) or isinstance(self.cells[y][x], type(self.predator)):
                    self.cells[y][x].moved = False

    def add_plankton(self):
        """Add additional portion of plankton"""
        num_additional_plankton = int((self.settings.num_rows + self.settings.num_cols))/10
        i = 0
        while i != num_additional_plankton:
            x = randint(0, self.settings.num_cols - 1)
            y = randint(0, self.settings.num_rows - 1)
            if self.cells[y][x] is None:
                self.cells[y][x] = Plankton(self, self.settings, x, y)
            else:
                continue
            i += 1
