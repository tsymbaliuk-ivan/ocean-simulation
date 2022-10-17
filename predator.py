from prey import Prey


class Predator(Prey):
    """Subclass Prey, predator, can move, breed, eat prey"""

    def __init__(self, settings):
        super().__init__(settings)
        self.time_to_feed = 6
        self.image = settings.image_for_predator
        self.number_of_element = settings.predators_number

    def process(self):
        """Проверяет time_to_feed, (если = 0 - смерть), иначе пытается сьесть добычу, в противном случае,
        перемещается в пустую ячейку, уменьшает time_to_reproduce на 1"""
        pass

    def reproduce(self, an_offset):
        """Воспроизвести себя в ячейку с координатами an_offset в массиве cells"""
        pass
