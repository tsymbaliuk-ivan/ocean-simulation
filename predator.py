from prey import Prey
import random


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

    def __find_nearest_preys_if_exist(self):

        all_neighbors = [self.west(), self.north(), self.south(), self.east()]
        preys = []
        # print(self.x, self.y)
        # print(all_neighbors)
        for neighbor in all_neighbors:
            if type(neighbor) == Prey:
                preys.append(neighbor)
                # print(f'neighbors = {neighbor.x},{neighbor.y}')
        return preys

    def __eat_nearest_prey(self, preys):

        prey = random.choice(preys)
        print(f'choise prey - {prey.x, prey.y}')  #######
        # сохраню старые координаты нашего текущего predator
        old_x = self.x
        old_y = self.y
        # поместим predator на место той рыбки, которую скушали
        self.ocean.cells[prey.y][prey.x] = self
        # освободим старое место
        self.ocean.cells[old_y][old_x] = None
        # присвоим новые координаты для нашего predator, которые были у жертвы
        self.x = prey.x
        self.y = prey.y
        # мы поели, значит не голодны до конца дня
        self.is_hungry = False

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""

        nearest_preys = self.__find_nearest_preys_if_exist()
        if nearest_preys:
            self.__eat_nearest_prey(nearest_preys)
        else:
            super().process()

    def set_predator_is_hungry(self):
        for y in range(self.ocean.num_rows):
            for x in range(self.ocean.num_cols):
                if type(self.ocean.cells[y][x]) == type(self):
                    self.ocean.cells[y][x].is_hungry = True

    def east(self):
        """Возвращает ячейку, на востоке от данной, если она есть"""
        if self.x + 1 < self.ocean.num_cols:
            return self.ocean.cells[self.y][self.x + 1]

    def north(self):
        """Возвращает ячейку, на севере от данной"""
        if self.y - 1 >= 0:
            return self.ocean.cells[self.y - 1][self.x]

    def south(self):
        """Возвращает ячейку, на юге от данной"""
        if self.y + 1 < self.ocean.num_rows:
            return self.ocean.cells[self.y + 1][self.x]

    def west(self):
        """Возвращает ячейку, на западе от данной"""
        if self.x - 1 >= 0:
            return self.ocean.cells[self.y][self.x - 1]


    def get_coord_for_all_predator(self):
        for x in range(self.ocean.num_rows):
            for y in range(len(self.ocean.cells[x])):
                if type(self.ocean.cells[x][y]) == Predator:
                    print(f'{self.ocean.cells[x][y]} x = {self.ocean.cells[x][y].x}, y = {self.ocean.cells[x][y].y}')

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass