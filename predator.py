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

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""

        if not self.eat_nearest_prey():
            print('move')
            super().process()
        # self.flag = False

    def get_coord_for_all_predator(self):
        for x in range(self.ocean.num_rows):
            for y in range(len(self.ocean.cells[x])):
                if type(self.ocean.cells[x][y]) == Predator:
                    print(f'{self.ocean.cells[x][y]} x = {self.ocean.cells[x][y].x}, y = {self.ocean.cells[x][y].y}')

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass

    # def set_predator_is_hungry(self, Predator):
    #     super().set_predator_is_hungry(Predator)

    def eat_nearest_prey(self):
        all_neighbors = [self.west(), self.north(), self.south(), self.east()]
        preys = []
        print(self.x, self.y)
        print(all_neighbors)
        for neighbor in all_neighbors:
            if type(neighbor) == Prey:
                preys.append(neighbor)

                print(f'neighbors = {neighbor.x},{neighbor.y}')  ####

        if preys:
            prey = random.choice(preys)

            print(f'choise prey - {prey.x, prey.y}')  #######
            # self.is_hungry = False
            # self.ocean.cells[prey.y][prey.x] = None
            # eat prey, занять новое место,
            old_x = self.x
            old_y = self.y
            self.ocean.cells[prey.y][prey.x] = self
            self.ocean.cells[old_y][old_x] = None
            # self.ocean.cells[self.y][self.x] = None
            self.x = prey.x
            self.y = prey.y

            # обьявить прошлое место пыстым в океане
            # self.ocean.cells[self.y][self.x] = None
            # не забыть изменить координаты, иначе они не будут не корректны
            # self.x = prey.x
            # self.y = prey.y

            # if self.ocean.cells[prey.y][prey.x]:
            #     self.ocean.cells[prey.y][prey.x].is_hungry = False
            # чтобы predator, когда тот ест рыбку справа или снизу, снова не вызывал метод process,
            # для фикса этого бага применяю флаг is_hungry, который сообщает о том, что predator на этой итерации
            # уже ел,
            # кормим рыбку, теперь она не голодная
            self.is_hungry = False

            return True
        else:
            return False

    def set_predator_is_hungry(self, predator):
        for y in range(self.ocean.num_rows):
            for x in range(self.ocean.num_cols):
                if type(self.ocean.cells[y][x]) == predator:
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
