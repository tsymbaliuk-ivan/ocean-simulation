from prey import Prey


class Predator(Prey):
    """Subclass Prey, predator, can move, breed, eat prey"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.time_to_feed = settings.time_to_feed
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number
        self.is_hungry = True

    def __repr__(self):
        return self.settings.image_for_predator

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""

        super().get_prey_neighbor_coord(Prey)
            # super().process()
        # self.flag = False

    def get_coord_for_all_predator(self):
        for x in range(self.ocean.num_rows):
            for y in range(len(self.ocean.cells[x])):
                if type(self.ocean.cells[x][y]) == Predator:
                    print(f'{self.ocean.cells[x][y]} x = {self.ocean.cells[x][y].x}, y = {self.ocean.cells[x][y].y}')

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass

    def set_predator_is_hungry(self, Predator):
        super().set_predator_is_hungry(Predator)