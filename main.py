from settings import Settings
from coordinate import Coordinate
from ocean import Ocean
from cell import Cell

ocean_settings = Settings()
cell = Cell()

ocean = Ocean(ocean_settings, cell, ocean_settings.num_rows, ocean_settings.num_cols, prey_number=150, predators_number=20, obstacles_number=75, )
ocean.create_ocean()
ocean.display_cells()


# ocean = []
# num_rows = 25
# num_cols = 75
# for y in range(num_rows):
#     ocean.append([])
#     for x in range(num_cols):
#         ocean[y].append('-')
#
# for x in range(num_rows):
#     for y in range(len(ocean[x])):
#         print(f'{ocean[x][y]}\t', end='')
#     print()
#
#
# ocean[1][3] = '*'
#
# for x in range(num_rows):
#     for y in range(len(ocean[x])):
#         print(f'{ocean[x][y]}\t', end='')
#     print()