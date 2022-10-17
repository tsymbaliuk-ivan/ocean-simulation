from cell import Cell


class Obstacle(Cell):
    """Преграда в океане, не может перемещаться"""
    def __init__(self, image):
        super(Obstacle, self).__init__(self, image)
        self.image = '#'
