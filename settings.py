from ui import UI


class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""

        self.number_iteration = 1000
        self.time_to_feed = 16
        self.time_to_feed_for_prey = 20
        self.time_to_reproduce_for_prey = 8
        self.time_to_reproduce_for_predator = 12
        self.time_to_reproduce_for_plankton = 10
        self.time_for_life_prey = 10
        self.time_for_life_plankton = 5
        self.prey_number = 120
        self.predators_number = 5
        self.obstacles_number = 50
        self.plankton_number = 100
        self.num_rows = 20
        self.num_cols = 40

        self.image_for_cell = '⁓'
        self.image_for_obstacle = '\033[37m⛰\033[0m'  # '🕳'#'🌿'#'⛰'
        self.image_for_prey = '\033[34m🐟\033[0m'
        self.image_for_predator = '\033[31m🦈\033[0m'
        self.image_for_plankton = '\033[32m🌿\033[0m' #🦠⁛

    def is_valid(self):
        sum_of_element = self.prey_number + self.obstacles_number + self.predators_number
        ocean_size = self.num_rows * self.num_cols
        if sum_of_element < ocean_size:
            return True
        UI.size_error()
        return False
