class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""
        self.prey_number = 2
        self.predators_number = 1
        self.obstacles_number = 1


        self.num_rows = 3
        self.num_cols = 4

        # self.num_rows = 25
        # self.num_cols = 75
        #
        # self.prey_number = 150
        # self.predators_number = 20
        # self.obstacles_number = 75

        self.image_for_cell = '⁓'
        self.image_for_obstacle = '⛰'
        self.image_for_prey = '\033[34m🐟\033[0m'
        self.image_for_predator = '\033[31m🦈\033[0m'
