from cell import Cell


class Obstacle(Cell):
    """Преграда в океане, не может перемещаться"""
    def __init__(self, settings):
        super().__init__()
        self.image = settings.image_for_obstacle
