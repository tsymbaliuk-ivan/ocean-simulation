class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""

        # self.num_rows = 25
        # self.num_cols = 75

        self.num_rows = 10
        self.num_cols = 20

        self.max_rows = 25
        self.max_cols = 75

        self.prey_number = 40
        self.predators_number = 10
        self.obstacles_number = 10

        self.image_for_obstacle = '⛰'
        self.image_for_prey = '\033[34m🐟\033[0m'
        self.image_for_predator = '\033[31m🦈\033[0m'
