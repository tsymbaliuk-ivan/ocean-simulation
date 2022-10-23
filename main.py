from settings import Settings
from ocean import Ocean
from prey import Prey
from predator import Predator

ocean_settings = Settings()
ocean = Ocean(ocean_settings)
ocean.run()
