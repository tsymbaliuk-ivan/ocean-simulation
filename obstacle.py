from cell import Cell


class Obstacle(Cell):
    """Ocean Obstacle, cannot move"""
    def __init__(self, ocean, settings, x, y):
        super().__init__(ocean, settings, x, y)
        self.image = settings.image_for_obstacle
        self.number_of_element = settings.obstacles_number
        self.x = x
        self.y = y
        self.settings = settings

    def __repr__(self):
        return self.settings.image_for_obstacle
