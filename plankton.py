from cell import Cell


class Plankton(Cell):
    """Subclass Cell, Plankton. Can be eaten"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.image = settings.image_for_plankton
        self.number_of_element = settings.plankton_number
        self.time_to_reproduce = settings.time_to_reproduce_for_plankton
        self.time_to_life = settings.time_for_life_plankton

    def __repr__(self):
        """Return image_for_prey"""
        return self.settings.image_for_plankton

    def process(self):
        """Decrements time_to_feed, time_to_reproduce.
        Moves to an empty cell. Checks time to feed, (if = 0 - death).
        Try to reproduce itself"""

        self.time_to_life -= 1
        self.time_to_reproduce -= 1
        if self.time_to_life <= 0:
            self.ocean.cells[self.y][self.x] = None
            self.settings.plankton_number -= 1
        if self.time_to_reproduce <= 0:
            empty_cell = super().find_neighbor_empty_cell(self)
            self.reproduce_to_neighbor_empty_cell(empty_cell)

    def reproduce_to_neighbor_empty_cell(self, empty_cell):
        if empty_cell:
            new_x = empty_cell[0]
            new_y = empty_cell[1]
            self.ocean.cells[new_y][new_x] = self
            self.ocean.cells[new_y][new_x].x = new_x
            self.ocean.cells[new_y][new_x].y = new_y
            return True
        return False
