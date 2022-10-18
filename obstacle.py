from cell import Cell


class Obstacle(Cell):
    """Ocean Obstacle, cannot move"""
    def __init__(self, settings, x=0, y=0):
        super().__init__(settings, x, y)
        self.image = settings.image_for_obstacle
        self.number_of_element = settings.obstacles_number
        self.x = x
        self.y = y
