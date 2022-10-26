from settings import Settings
from ocean import Ocean

ocean_settings = Settings()
if ocean_settings.is_valid():
    ocean = Ocean(ocean_settings)
    ocean.run()
