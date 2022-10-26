from cell import Cell
import random

class Prey(Cell):
    """Subclass Cell, prey. Can move, breed and be eaten"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.image = settings.image_for_prey
        self.number_of_element = settings.prey_number
        self.time_to_reproduce = settings.time_to_reproduce_for_prey
        self.time_for_life_prey = settings.time_for_life_prey
        self.time_to_feed = settings.time_to_feed_for_prey

    def __repr__(self):
        """Return image_for_prey"""
        return self.settings.image_for_prey

    # def process(self):
    #     """Decrements time_to_feed, time_to_reproduce.
    #     Moves to an empty cell. Checks time to feed, (if = 0 - death).
    #     Try to reproduce itself"""
    #
    #     self.time_to_reproduce -= 1
    #     self.time_to_feed -= 1
    #     old_x = self.x
    #     old_y = self.y
    #     if super().move_to_neighbor_empty_cell(self):
    #         self.moved = True
    #         self.ocean.try_to_reproduce_fish(self, old_x, old_y)
    #     if self.time_to_feed <= 0:
    #         self.ocean.cells[self.y][self.x] = None
    #         self.settings.prey_number -= 1

    def find_neighbor_plankton_if_exist(self) -> list:
        """Find nearest plankton if exist"""
        all_neighbors = self.ocean.find_neighbors(self)
        neighbor_plankton = []
        for neighbor in all_neighbors:
            if isinstance(neighbor, type(self.ocean.plankton)):
                neighbor_plankton.append(neighbor)
        return neighbor_plankton

    def eat_nearest_plankton(self, preys):
        """Eat nearest prey, random choice prey from preys list.
        Increase time to feed, set predator is not hungry """
        prey = random.choice(preys)
        old_x = self.x  # сохраню старые координаты нашего текущего predator
        old_y = self.y
        self.x = prey.x
        self.y = prey.y
        self.ocean.cells[prey.y][prey.x] = self  # поместим predator на место той рыбки, которую скушали
        self.ocean.cells[old_y][old_x] = None  # освободим старое место
        self.time_for_life_prey += 1

    def process(self):
        """Decrements time_to_feed, time_to_reproduce.
        Checks time to feed, (if = 0 - death), otherwise tries to eat prey, otherwise,
        moves to an empty cell. Checks already_moving, (if <= 0 - pass), set already_moving - True.
        And try to reproduce itself"""
        self.time_for_life_prey -= 1
        self.time_to_reproduce -= 1
        self.time_to_feed -= 1
        old_x = self.x
        old_y = self.y

        if self.time_for_life_prey <= 0 or self.time_to_feed <=0:
            self.ocean.cells[self.y][self.x] = None
            self.settings.prey_number -= 1

        elif self.moved is False:  # Prey еще не ел и не двигался
            neighbor_plankton = self.find_neighbor_plankton_if_exist()  # найти жертву, если такая есть
            if neighbor_plankton:
                self.eat_nearest_plankton(neighbor_plankton)
                self.time_to_feed += 1
                self.settings.plankton_number -= 1
            else:
                super().move_to_neighbor_empty_cell(self)
                self.ocean.try_to_reproduce_fish(self, old_x, old_y)  # размножатся, если получиться
            self.moved = True
