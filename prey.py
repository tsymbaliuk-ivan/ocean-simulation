from cell import Cell

class Prey(Cell):
    """подкласс Cell, добыча. Может перемещаться, размножаться и быть сьеденой"""

    default_pray_image = 'f'
    time_to_reproduce = 6
    def __init__(self):

        self.time_to_reproduce = 6