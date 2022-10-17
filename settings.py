class Settings:
    """A class to store all settings """

    def __init__(self):
        """Initialize settings."""

        # self.num_rows = 25
        # self.num_cols = 75

        self.num_rows = 6
        self.num_cols = 10

        self.max_rows = 25
        self.max_cols = 75
        self.prey_number = 150
        self.predators_number = 20
        self.obstacles_number = 5

        self.image_for_obstacle = '#'