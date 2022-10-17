from settings import Settings
from coordinate import Coordinate
from ocean import Ocean
from cell import Cell
from obstacle import Obstacle

cell = Cell()
ocean_settings = Settings()
obstacle = Obstacle(ocean_settings)


ocean = Ocean(ocean_settings)
ocean.create_ocean(cell)
ocean.add_obstacles(obstacle, cell)
ocean.display_cells()


