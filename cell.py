from generator_x_y import GeneratorXY

class Cell:
    """Cell - superclass for all kinds of cells that are in the ocean"""

    def __init__(self, ocean, settings, x, y):
        self.x = x
        self.y = y
        self.ocean = ocean
        self.settings = settings
        self.is_hungry = True
        self.already_moving = False

    def __repr__(self):
        return

    def process(self, fish):
        """Перемещает в соседнюю ячейку, используя определенные правила (в зависимости от подкласса)"""

        fish.time_to_reproduce -= 1
        fish.time_to_feed -= 1
        old_x = fish.x
        old_y = fish.y

        if type(fish) == type(self.ocean.predator):
            if fish.already_moving == False:
                nearest_preys = fish.find_nearest_preys_if_exist()
                if nearest_preys:
                    fish.eat_nearest_prey(nearest_preys)
                else:
                    new_x, new_y = GeneratorXY.generate_new_coord(self)
                    if self.ocean.cells[new_y][new_x] is None:
                        self.ocean.cells[fish.y][fish.x] = None
                        self.ocean.cells[new_y][new_x] = fish
                        self.ocean.cells[new_y][new_x].x = new_x
                        self.ocean.cells[new_y][new_x].y = new_y
                    if fish.time_to_reproduce <= 0 and self.ocean.cells[old_y][old_x] is None:
                        self.ocean.cells[old_y][old_x] = self.ocean.initialize_predator(old_x, old_y)
                        fish.time_to_reproduce = self.settings.time_to_reproduce_for_predator

        self.already_moving = True
        if type(fish) == type(self.ocean.prey):
            fish.marker += 1
            print(fish.marker)
            new_x, new_y = GeneratorXY.generate_new_coord(self)
            if self.ocean.cells[new_y][new_x] is None:
                self.ocean.cells[fish.y][fish.x] = None
                self.ocean.cells[new_y][new_x] = fish
                self.ocean.cells[new_y][new_x].x = new_x
                self.ocean.cells[new_y][new_x].y = new_y

            if fish.time_to_feed <= 0:
                self.ocean.cells[fish.y][fish.x] = None

            if fish.time_to_reproduce <= 0 and self.ocean.cells[old_y][old_x] == None:
                self.ocean.cells[old_y][old_x] = self.ocean.initialize_prey(old_x, old_y)
                fish.time_to_reproduce = fish.settings.time_to_reproduce_for_prey
                fish.marker += 1



    def get_cell_at(self, a_coord):
        """Возвращает ячейку с координатами a_coord в массиве cells из ocean"""
        pass

    def assign_cell_at(self, a_coord, a_cell):
        """Помещает ячейку a_cell в место с координатоми a_coord в массиве cells"""
        pass

    def get_off_set(self):
        """Возвращает смещение"""
        pass

    def set_off_set(self, a_coord):
        """Устанавливает смещение в a_coord"""
        pass

    def get_image(self):
        """return image"""
        pass

    def display(self):
        """Выводит изображение по соответствующему смещению"""
        pass
