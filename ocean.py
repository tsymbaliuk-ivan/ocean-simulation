from random import randint


class Ocean:
    """Ocean is a 2D cell array. The ocean has prey, predators, obstacles and empty cell"""
    cells = []

    def __init__(self, settings):
        self.num_rows = settings.num_rows
        self.num_cols = settings.num_cols
        self.prey_number = settings.prey_number
        self.predators_number = settings.predators_number
        self.obstacles_number = settings.obstacles_number

    def get_num_prey(self):
        """return number of prey"""
        pass

    def set_num_prey(self, a_number):
        """set number of prey"""
        self.prey_number = a_number

    def get_num_predators(self):
        """return number of predators"""

        return self.predators_number

    def initialize(self):
        """init size ocean, prey, predator, obstacle"""
        pass

    def init_cells(self, obstacles_number, prey_number, predators_number):
        self.prey_number = prey_number
        self.predators_number = predators_number
        self.obstacles_number = obstacles_number

    def add_inhabitants(self, obstacles, prey, predator, cell):
        """Добавим обитателей океана, включая препятствия"""
        ocean_elements = obstacles, prey, predator
        for ocean_element in ocean_elements:
            self.add_element(ocean_element, cell)

    def add_element(self, ocean_element, cell):
        """Будем заполнять cells"""
        i = 0
        while i != ocean_element.number_of_element:
            x = randint(0, self.num_cols - 1)
            y = randint(0, self.num_rows - 1)
            if type(self.cells[y][x]) == type(cell):
                self.cells[y][x] = ocean_element
            else:
                continue
            i += 1

    def add_predators(self, num_predators):
        self.predators_number = num_predators

    def add_prey(self, num_prey):
        self.prey_number = num_prey

    def display_border(self):
        """отображает максимальную ограниченную область океана (горизонтальная граница)"""
        pass

    def display_cells(self):
        """пересчитывает и выводит массив cells"""

        for x in range(self.num_rows):
            for y in range(len(self.cells[x])):
                print(f'{self.cells[x][y]}\t', end='')
            print()

    def display_stats(self):
        """Обновляет отображаемый номер итерации, количество преград, хищников и добычи"""
        pass

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        pass

    def create_ocean(self, cell):

        # заполним все места пробелами
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                self.cells[y].append(cell)
