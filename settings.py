class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""
        self.prey_number = 100
        self.predators_number = 10

        self.obstacles_number = 10

        self.num_rows = 10
        self.num_cols = 20

        # self.num_rows = 25
        # self.num_cols = 75
        #
        # self.prey_number = 150
        # self.predators_number = 20
        # self.obstacles_number = 75
        #
        # self.num_rows = 10
        # self.num_cols = 30
        #
        # self.prey_number = 25
        # self.predators_number = 10
        # self.obstacles_number = 10

        self.image_for_cell = '⁓'
        self.image_for_obstacle = '\033[32m🌿\033[0m' #'🕳'#'🌿'#'⛰'
        self.image_for_prey = '\033[34m🐟\033[0m'
        self.image_for_predator = '\033[31m🦈\033[0m'

        self.time_to_feed = 6
        self.time_to_reproduce_for_prey = 5
        self.time_to_reproduce_for_predator = 6
        self.time_for_life_prey = 8