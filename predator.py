from prey import Prey
import random


class Predator(Prey):
    """Subclass Prey, predator, can move, breed, eat prey"""

    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.time_to_feed = settings.time_to_feed
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number

    def __repr__(self):
        return self.settings.image_for_predator

    def __find_nearest_preys_if_exist(self):

        all_neighbors = [self.west(), self.north(), self.south(), self.east()]
        preys = []
        for neighbor in all_neighbors:
            if type(neighbor) == Prey:
                preys.append(neighbor)

        return preys

    def __eat_nearest_prey(self, preys):


        prey = random.choice(preys)
        # сохраню старые координаты нашего текущего predator
        old_x = self.x
        old_y = self.y
        self.x = prey.x
        self.y = prey.y
        # поместим predator на место той рыбки, которую скушали
        self.ocean.cells[prey.y][prey.x] = self
        # освободим старое место
        self.ocean.cells[old_y][old_x] = None
        # присвоим новые координаты для нашего predator, которые были у жертвы
        # self.x = prey.x
        # self.y = prey.y
        # мы поели, значит не голодны до конца дня
        self.is_hungry = False
        self.time_to_feed += 1

        # print('ate')
        # print(f'predator x = {self.x}, y = {self.y}')

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""
        self.time_to_feed -= 1

        if self.time_to_feed <= 0:
            self.ocean.cells[self.y][self.x] = None

        else:
            nearest_preys = self.__find_nearest_preys_if_exist()
            if nearest_preys:
                print(f'predator x = {self.x}, y = {self.y}')
                self.__eat_nearest_prey(nearest_preys)
                print(f'eat nearest prey x = {self.x}, y = {self.y}')

            else:
                print(f'predator x = {self.x}, y = {self.y}')
                print('only move')
                if self.already_moving == False:
                    super().process()
                    print(f'coord after move x = {self.x}, y = {self.y}')
                else:
                    pass

            # else:
            #     print(f'coord before move x = {self.x}, y = {self.y}')
            #     print('only move')
            #     super().process()
            #     print(f'coord after move x = {self.x}, y = {self.y}')
        self.already_moving = True
        print(f'time_to_feed  = {self.time_to_feed}')

    def set_predator_is_hungry(self):
        for y in range(self.ocean.num_rows):
            for x in range(self.ocean.num_cols):
                if type(self.ocean.cells[y][x]) == type(self):
                    self.ocean.cells[y][x].is_hungry = True

    def set_alredy_moving(self):
        for y in range(self.ocean.num_rows):
            for x in range(self.ocean.num_cols):
                if type(self.ocean.cells[y][x]) == type(self):
                    self.ocean.cells[y][x].already_moving = False

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