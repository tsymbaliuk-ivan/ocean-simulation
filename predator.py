from prey import Prey

class Predator(Prey):
    """подкласс Prey, хищник, может перемещаться, размножаться, есть добычу"""

    default_predator_image = 'S'
    time_to_feed = 6
