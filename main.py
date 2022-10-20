from settings import Settings
from ocean import Ocean
from obstacle import Obstacle
from prey import Prey
from predator import Predator

ocean_settings = Settings()
ocean = Ocean(ocean_settings)
predator = Predator(ocean, ocean_settings, 0, 0)
obstacle = Obstacle(ocean, ocean_settings)
prey = Prey(ocean, ocean_settings, 0, 0)


ocean.create_ocean()
ocean.add_inhabitants(obstacle, prey, predator, ocean_settings)


ocean.display_cells(ocean_settings)
ocean.process()
ocean.display_cells(ocean_settings)
print()
predator.set_predator_is_hungry(Predator)
ocean.process()
ocean.display_cells(ocean_settings)

print()
predator.set_predator_is_hungry(Predator)
ocean.process()
ocean.display_cells(ocean_settings)

print()
predator.set_predator_is_hungry(Predator)
ocean.process()
ocean.display_cells(ocean_settings)


# predator.set_predator_is_hungry(Predator)
# ocean.display_cells(ocean_settings)
# ocean.process()
# print()
# ocean.display_cells(ocean_settings)


# ocean.display_cells(ocean_settings)
# ocean.process()
# print()
# ocean.display_cells(ocean_settings)



