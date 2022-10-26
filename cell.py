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

    def find_neighbor_empty_cell(self, cell) -> tuple:
        neighbor_cells_list = self.ocean.find_neighbors(cell)
        none_neighbor_cells = []
        for neighbor in neighbor_cells_list:
            if isinstance(neighbor, tuple):
                none_neighbor_cells.append(neighbor)

        if len(none_neighbor_cells) > 1:
            empty_cell = random.choice(none_neighbor_cells)
            return empty_cell

        elif none_neighbor_cells:
            return none_neighbor_cells[0][0], none_neighbor_cells[0][1]

    def move_to_neighbor_empty_cell(self, cell):
        empty_cell = self.find_neighbor_empty_cell(cell)
        if empty_cell:
            new_x = empty_cell[0]
            new_y = empty_cell[1]
            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[new_y][new_x] = self
            self.ocean.cells[new_y][new_x].x = new_x
            self.ocean.cells[new_y][new_x].y = new_y
            return True
        return False

    # def make_a_move(self):
    #     """Moves to cell using certain rules"""
    #     new_x, new_y = GeneratorXY.generate_new_coord(self)
    #     if self.ocean.cells[new_y][new_x] is None:
    #         self.ocean.cells[self.y][self.x] = None
    #         self.ocean.cells[new_y][new_x] = self
    #         self.ocean.cells[new_y][new_x].x = new_x
    #         self.ocean.cells[new_y][new_x].y = new_y
