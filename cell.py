from generator_x_y import GeneratorXY
import random


class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""

    def __init__(self, ocean, settings, x, y):
        self.x = x
        self.y = y
        self.ocean = ocean
        self.settings = settings
        self.moved = False  # нам надо знать, двигалась рыба на итерации или нет

    def __repr__(self):
        """Return None"""
        return

    def make_a_move(self):
        """Moves to cell using certain rules"""
        new_x, new_y = GeneratorXY.generate_new_coord(self)
        if self.ocean.cells[new_y][new_x] is None:
            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[new_y][new_x] = self
            self.ocean.cells[new_y][new_x].x = new_x
            self.ocean.cells[new_y][new_x].y = new_y

    def find_neighbor_empty_cell(self, cell):
        neighbor_cells = self.ocean.find_neighbors(cell)
        print(neighbor_cells)
        none_neighbor_cells = []
        for neighbor in neighbor_cells:
            if isinstance(neighbor, type(None)):
                none_neighbor_cells.append(neighbor)

        empty_cell = random.choice(none_neighbor_cells)
        return empty_cell
