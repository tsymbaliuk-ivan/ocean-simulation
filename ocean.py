from random import randint

class Ocean:
    """Ocean - двумерный массив ячеек. В океане есть добыча, хищники, преграды и пустые ячейки"""

    max_rows = 25
    num_rows = 25
    max_cols = 75
    num_cols = 75
    def __init__(self, num_rows,num_cols, prey_number, predators_number, obstacles_number):
    # двумерный массив ячеек
    # cells =

        self.size = num_cols * num_rows
        self.prey_number = 150
        self.predators_number = 20
        self.obstacles_number = 75

    def get_num_prey(self):
        """return number of prey"""
        pass


    def set_num_prey(self, number):
        """set number of prey"""
        self.prey_number = number


    def get_num_predators(self):
        """return number of predators"""

        return self.predators_number


    def initialize(self):
        """init size ocean, prey, predator, obstacle"""

        self.num_cols = randint(10, 75)
        self.num_rows = randint(5, 25)
        self.prey_number = randint(125, 175)
        self.predators_number = randint(10, 30)
        self.obstacles_number = randint(50, 100)


    def init_cells(self, obstacles_number, prey_number, predators_number):
        self.prey_number = prey_number
        self.predators_number = predators_number
        self.obstacles_number = obstacles_number


    def add_obstacles(self, num_obstacles):
        self.obstacles_number = num_obstacles


    def add_predators(self, num_predators):
        self.predators_number = num_predators


    def add_prey(self, num_prey):
        self.prey_number = num_prey


    def display_border(self):
        """отображает максимальную ограниченную область океана (горизонтальная граница)"""
        pass

    def displat_cells(self):
        """пересчитывает и выводит массив cells"""
        pass

    def display_stats(self):
        """Обновляет отображаемый номер итерации, количество преград, хищников и добычи"""
        pass

    def run(self):
        """Запрашивает у пользователя количество итераций и начинает моделирование"""
        pass



