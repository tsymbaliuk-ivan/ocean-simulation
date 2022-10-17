from cell import Cell


class Obstacle(Cell):
    """Ocean Obstacle, cannot move"""
    def __init__(self, settings):
        super().__init__(settings)
        self.image = settings.image_for_obstacle
        self.number_of_element = settings.obstacles_number
