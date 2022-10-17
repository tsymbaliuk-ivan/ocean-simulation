

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
