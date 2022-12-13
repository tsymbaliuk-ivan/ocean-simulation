from settings import Settings
from ocean import Ocean

if __name__ == '__main__':
    ocean_settings = Settings()
    ocean = Ocean(ocean_settings)
    ocean.run()
