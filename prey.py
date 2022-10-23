from cell import Cell


class Prey(Cell):
    """Subclass Cell, prey. Can move, breed and be eaten"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.image = settings.image_for_prey
        self.number_of_element = settings.prey_number
        self.time_to_reproduce = settings.time_to_reproduce_for_prey
        self.time_for_life = settings.time_for_life_prey
    def __repr__(self):
        return self.settings.image_for_prey

    def process(self):
        """Перемещается, если возможно в пустую ячейку и уменьшает time_to_reproduce на 1"""
        old_x = self.x
        old_y = self.y
        super().process()
        self.time_to_reproduce -= 1
        self.time_for_life -= 1

        if self.time_for_life <= 0:
            self.ocean.cells[self.y][self.x] = None

        elif self.time_to_reproduce <= 0 and self.ocean.cells[old_y][old_x] is None:
            self.ocean.cells[old_y][old_x] = Prey(self.ocean, self.settings, old_x, old_y)
            self.time_to_reproduce = self.settings.time_to_reproduce_for_prey

    def move_from(self, from_coord, to_coord):
        """Перемещает из координаты from_coord, в координаты to_coord в массиве cells"""
        pass

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass
