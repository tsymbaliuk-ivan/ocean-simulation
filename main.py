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


# ocean.get_coord_for_all_prey()
# predator.get_coord_for_all_predator()

ocean.process()
print()
ocean.display_cells(ocean_settings)

# ocean.get_coord_for_all_prey()
# predator.get_coord_for_all_predator()



# ocean.get_coord_for_all_prey(prey)
# ocean.process(prey, ocean_settings)
# print('process')
# ocean.display_cells()
# ocean.get_coord_for_all_prey(prey)


