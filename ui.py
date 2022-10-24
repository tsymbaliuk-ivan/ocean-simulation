class UI:

    @staticmethod
    def get_number_iteration():
        """Get number of iteration"""

        number_iteration = int(input('Enter positive,int number of iterations: '))
        return number_iteration

    @staticmethod
    def show_cells(ocean):
        """Print all cells"""

        print('\t', end='')
        print('\033[34m⥎\033[0m\t' * ocean.num_cols)
        for x in range(ocean.num_rows):
            print('\033[34m⥑\033[0m\t', end='')
            for y in range(len(ocean.cells[x])):
                if ocean.cells[x][y]:
                    print(f'{ocean.cells[x][y]}\t', end='')
                else:
                    print(f'{ocean.settings.image_for_cell}\t', end='')
            print('\033[34m⥏\033[0m\t', end='')
            print()
        print('\t', end='')
        print('\033[34m⥐\033[0m\t' * ocean.num_cols)

    @staticmethod
    def display_stats(ocean, iteration):
        return (print(f'preys = {ocean.prey_number}, predators = {ocean.predators_number}, '
                f'obstacles = {ocean.obstacles_number}'), print(f'iteration {iteration}'))


    @staticmethod
    def print_border(ocean):
        print()
        print('⁕\t' * ocean.num_cols, '⁕\t')
        print()

    @staticmethod
    def finish_simulation(ocean, iteration):
        print(f'finished at iteration {iteration} -', end=' ')

        if ocean.predators_number <= 0:
            print('all predators are dead')
        elif ocean.prey_number <= 0:
            print('all the preys are dead')
        else:
            print('balance is maintained')
