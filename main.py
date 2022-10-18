from settings import Settings
from coordinate import Coordinate
from ocean import Ocean
from cell import Cell
from obstacle import Obstacle
from prey import Prey
from predator import Predator


ocean_settings = Settings()
cell = Cell(ocean_settings)
predator = Predator(ocean_settings)
obstacle = Obstacle(ocean_settings)
prey = Prey(ocean_settings)
ocean = Ocean(ocean_settings)

ocean.create_ocean(cell)
ocean.add_inhabitants(obstacle, prey, predator, cell)

ocean.display_cells()

#
# ocean.process(prey, cell)
#
# print()
# ocean.display_cells()

