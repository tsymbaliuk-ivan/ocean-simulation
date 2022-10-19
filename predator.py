from prey import Prey


class Predator(Prey):
    """Subclass Prey, predator, can move, breed, eat prey"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.time_to_feed = 6
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number

    def __repr__(self):
        return self.settings.image_for_predator

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""
        # super().find_prey(self, Prey)
        # print(self.x, self.y)
        # if self.time_to_feed > 0:
        #     if super().find_prey():
        #         super.eat_prey()
        #     else:
        #         super().move_in_free_cell()
        #         self.time_to_feed -= 1
        # super().process()
        # print(self.x, self.y)

    def get_coord_for_all_predator(self):
        for x in range(self.ocean.num_rows):
            for y in range(len(self.ocean.cells[x])):
                if type(self.ocean.cells[x][y]) == Predator:
                    print(f'{self.ocean.cells[x][y]} x = {self.ocean.cells[x][y].x}, y = {self.ocean.cells[x][y].y}')

    # def get_coord_current_predetaor(self):
    #     print(self.x, self.y)

    # def find_neighbors(self):
    #     all_neighbor = [self.east()]
    #     print(all_neighbor)
    #
    # def east(self):
    #     """Возвращает ячейку, на востоке от данной"""
    #     if self.x + 1 < self.ocean.num_cols:
    #         # print(self.ocean.cells[self.y][self.x])
    #         # print(self.x, self.y)
    #         return self.ocean.cells[self.y][self.x]

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass

