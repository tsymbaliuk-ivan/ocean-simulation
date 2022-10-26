import random
from cell import Cell


class Predator(Cell):
    """Subclass Cell, predator, can move, breed, eat prey"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.time_to_feed = settings.time_to_feed
        self.time_to_reproduce = settings.time_to_reproduce_for_predator
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number

    def __repr__(self):
        """Return image_for_predator"""
        return self.settings.image_for_predator

    def find_neighbor_preys_if_exist(self) -> list:
        """Find nearest preys if exist"""
        all_neighbors = self.ocean.find_neighbors(self)
        neighbor_preys = []
        for neighbor in all_neighbors:
            if isinstance(neighbor, type(self.ocean.prey)):
                neighbor_preys.append(neighbor)
        return neighbor_preys

    def eat_nearest_prey(self, preys):
        """Eat nearest prey, random choice prey from preys list.
        Increase time to feed, set predator is not hungry """
        prey = random.choice(preys)
        old_x = self.x  # сохраню старые координаты нашего текущего predator
        old_y = self.y
        self.x = prey.x
        self.y = prey.y
        self.ocean.cells[prey.y][prey.x] = self  # поместим predator на место той рыбки, которую скушали
        self.ocean.cells[old_y][old_x] = None  # освободим старое место
        self.time_to_feed += 1

    def process(self):
        """Decrements time_to_feed, time_to_reproduce.
        Checks time to feed, (if = 0 - death), otherwise tries to eat prey, otherwise,
        moves to an empty cell. Checks already_moving, (if <= 0 - pass), set already_moving - True.
        And try to reproduce itself"""
        self.time_to_feed -= 1
        self.time_to_reproduce -= 1
        old_x = self.x
        old_y = self.y

        if self.time_to_feed <= 0:
            self.ocean.cells[self.y][self.x] = None
            self.settings.predators_number -= 1

        elif self.moved is False:  # Predator еще не ел и не двигался
            neighbor_preys = self.find_neighbor_preys_if_exist()  # найти жертву, если такая есть
            if neighbor_preys:
                self.eat_nearest_prey(neighbor_preys)
                self.settings.prey_number -= 1
            else:
                print(super().find_neighbor_empty_cell(self))
                super().make_a_move()  # жертв нет, только двигаться
                self.ocean.try_to_reproduce_fish(self, old_x, old_y)  # размножатся, если получиться
            self.moved = True

