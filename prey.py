from cell import Cell


class Prey(Cell):
    """Подкласс Cell, добыча. Может перемещаться, размножаться и быть сьеденой"""
    # default_pray_image = 'f'
    # time_to_reproduce = 6
    def __init__(self, settings):
        super().__init__()
        self.image = settings.image_for_prey
        self.time_to_reproduce = 6
        self.number_of_element = settings.prey_number


    def process(self):
        """Перемещается, если возможно в пустую ячейку и уменьшает time_to_reproduce на 1"""
        pass

    def move_from(self, from_coord, to_coord):
        """Перемещает из координаты from_coord, в координаты to_coord в массиве cells"""
        pass

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass

