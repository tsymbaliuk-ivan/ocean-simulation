from cell import Cell


class Prey(Cell):
    """Subclass Cell, prey. Can move, breed and be eaten"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.image = settings.image_for_prey
        self.number_of_element = settings.prey_number
        self.time_to_reproduce = settings.time_to_reproduce_for_prey
        self.time_to_feed = settings.time_for_life_prey

    def __repr__(self):
        """Return image_for_prey"""
        return self.settings.image_for_prey

    def process(self):
        """Decrements time_to_feed, time_to_reproduce.
        Moves to an empty cell. Checks time to feed, (if = 0 - death).
        Try to reproduce itself"""

        self.time_to_reproduce -= 1
        self.time_to_feed -= 1
        old_x = self.x
        old_y = self.y
        if super().move_to_neighbor_empty_cell(self):
            self.moved = True
            self.ocean.try_to_reproduce_fish(self, old_x, old_y)
        if self.time_to_feed <= 0:
            self.ocean.cells[self.y][self.x] = None
            self.settings.prey_number -= 1

    def move_from(self, from_coord, to_coord):
        """Перемещает из координаты from_coord, в координаты to_coord в массиве cells"""
        pass
