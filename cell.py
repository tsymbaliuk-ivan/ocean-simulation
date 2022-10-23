from generator_x_y import GeneratorXY

class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""

    def __init__(self, ocean, settings, x, y):
        self.x = x
        self.y = y
        self.ocean = ocean
        self.settings = settings
        self.is_hungry = True
        self.already_moving = False

    def __repr__(self):
        return

    def process(self):
        """Перемещает в соседнюю ячейку, используя определенные правила (в зависимости от подкласса)"""
        new_x, new_y = GeneratorXY.generate_new_coord(self)

        if self.ocean.cells[new_y][new_x] is None:
            self.ocean.cells[self.y][self.x] = None
            self.ocean.cells[new_y][new_x] = self
            self.ocean.cells[new_y][new_x].x = new_x
            self.ocean.cells[new_y][new_x].y = new_y

            return True

        return False

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
