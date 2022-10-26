class UI:

    @staticmethod
    def get_num_cols():
        num_cols = int(input('Enter num_cols: '))
        return num_cols

    @staticmethod
    def get_num_rows():
        num_rows = int(input('Enter num_rows: '))
        return num_rows

    @staticmethod
    def get_obstacles_number():
        obstacles_number = int(input('Enter obstacles_number: '))
        return obstacles_number

    @staticmethod
    def get_predators_number():
        predators_number = int(input('Enter predators_number: '))
        return predators_number

    @staticmethod
    def get_prey_number():
        prey_number = int(input('Enter prey_number : '))
        return prey_number

    @staticmethod
    def get_time_for_life_prey():
        time_for_life_prey = int(input('Enter time_for_life_prey : '))
        return time_for_life_prey

    @staticmethod
    def get_time_to_reproduce_for_predator():
        time_to_reproduce_for_predator = int(input('Enter time_to_reproduce_for_predator: '))
        return time_to_reproduce_for_predator

    @staticmethod
    def get_time_to_reproduce_for_prey():
        time_to_reproduce_for_prey = int(input('Enter time_to_reproduce_for_prey: '))
        return time_to_reproduce_for_prey

    @staticmethod
    def get_time_to_feed():
        time_to_feed = int(input('Enter time_to_feed for predator: '))
        return time_to_feed

    @staticmethod
    def get_number_iteration():
        """Get number of iteration"""
        number_iteration = int(input('Enter positive,int number of iterations: '))
        return number_iteration

    @staticmethod
    def show_cells(ocean):
        """Print all cells"""

        print('\t', end='')
        print('\033[34m⥎\033[0m\t' * ocean.settings.num_cols)
        for x in range(ocean.settings.num_rows):
            print('\033[34m⥑\033[0m\t', end='')
            for y in range(len(ocean.cells[x])):
                if ocean.cells[x][y]:
                    print(f'{ocean.cells[x][y]}\t', end='')
                else:
                    print(f'{ocean.settings.image_for_cell}\t', end='')
            print('\033[34m⥏\033[0m\t', end='')
            print()
        print('\t', end='')
        print('\033[34m⥐\033[0m\t' * ocean.settings.num_cols)

    @staticmethod
    def display_stats(ocean, iteration):
        return (print(f'preys = {ocean.settings.prey_number}, predators = {ocean.settings.predators_number}, '
                      f'obstacles = {ocean.settings.obstacles_number}'), print(f'iteration {iteration}'))

    @staticmethod
    def print_border(ocean):
        print()
        print('⁕\t' * ocean.settings.num_cols, '⁕\t')
        print()

    @staticmethod
    def finish_simulation(ocean, iteration):
        print()
        print(f'finished at iteration {iteration} -', end=' ')

        if ocean.settings.predators_number <= 0:
            print('all predators are dead')
        elif ocean.settings.prey_number <= 0:
            print('all the preys are dead')
        else:
            print('balance is maintained')

    @staticmethod
    def size_error():
        print('The size of the ocean is less than necessary')
