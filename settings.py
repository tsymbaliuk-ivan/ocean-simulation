from ui import UI


class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""
        self.number_iteration = UI.get_number_iteration()
        self.time_to_feed = UI.get_time_to_feed()
        self.time_to_reproduce_for_prey = UI.get_time_to_reproduce_for_prey()
        self.time_to_reproduce_for_predator = UI.get_time_to_reproduce_for_predator()
        self.time_for_life_prey = UI.get_time_for_life_prey()
        self.prey_number = UI.get_prey_number()
        self.predators_number = UI.get_predators_number()
        self.obstacles_number = UI.get_obstacles_number()
        self.num_rows = UI.get_num_rows()
        self.num_cols = UI.get_num_cols()

        # self.number_iteration = 50
        # self.time_to_feed = 10
        # self.time_to_reproduce_for_prey = 12
        # self.time_to_reproduce_for_predator = 8
        # self.time_for_life_prey = 20
        # self.prey_number = 50
        # self.predators_number = 10
        # self.obstacles_number = 10
        # self.num_rows = 10
        # self.num_cols = 20

        # self.num_rows = 25
        # self.num_cols = 75
        # self.prey_number = 150
        # self.predators_number = 20
        # self.obstacles_number = 75
        # self.num_rows = 10
        # self.num_cols = 30
        # self.prey_number = 25
        # self.predators_number = 10
        # self.obstacles_number = 10

        self.image_for_cell = '⁓'
        self.image_for_obstacle = '\033[32m🌿\033[0m'  # '🕳'#'🌿'#'⛰'
        self.image_for_prey = '\033[34m🐟\033[0m'
        self.image_for_predator = '\033[31m🦈\033[0m'
