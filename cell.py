from generator_x_y import GeneratorXY
# from prey import Prey
# from predator import Predator


class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""

    def __init__(self, ocean, settings, x, y):
        self.x = x
        self.y = y
        self.ocean = ocean
        self.settings = settings
        self.is_hungry = True  # надо знать, ел ли predator на итерации или нет
        self.already_moving = False  # нам надо знать, двигалась слетка на итерации или нет

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

    def try_to_reproduce(self, fish, old_x, old_y):
        """Reproduce yourself to the cell with coordinates old_x, old_y in the cells array"""
        if fish.time_to_reproduce <= 0 and self.ocean.cells[old_y][old_x] is None:
            if isinstance(fish, self.ocean.prey_):
                self.ocean.cells[old_y][old_x] = self.ocean.prey_(self.ocean, self.settings, old_x, old_y)
                self.ocean.prey_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_prey

            elif isinstance(fish, self.ocean.predator_):
                self.ocean.cells[old_y][old_x] = self.ocean.predator_(self.ocean, self.settings, old_x, old_y)
                self.ocean.predators_number += 1
                fish.time_to_reproduce = self.settings.time_to_reproduce_for_predator

    def get_cell_at(self, a_coord):
        """Возвращает ячейку с координатами a_coord в массиве cells из ocean"""
        pass

    def assign_cell_at(self, a_coord, a_cell):
        """Помещает ячейку a_cell в место с координатоми a_coord в массиве cells"""
        pass

    def get_off_set(self):
        """Возвращает смещение"""
        pass

    def set_off_set(self, a_coord):
        """Устанавливает смещение в a_coord"""
        pass

    def get_image(self):
        """return image"""
        pass

    def display(self):
        """Выводит изображение по соответствующему смещению"""
        pass


