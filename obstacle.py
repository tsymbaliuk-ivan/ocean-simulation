from cell import Cell


class Obstacle(Cell):
    """Преграда в океане, не может перемещаться"""
    def __init__(self, settings):
        super().__init__()
        self.image = settings.image_for_obstacle
        self.number_of_element = settings.obstacles_number
