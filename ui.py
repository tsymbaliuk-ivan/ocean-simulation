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
    def display_stats(ocean):
        return (print(f'preys = {ocean.prey_number}, predators = {ocean.predators_number}, '
                f'obstacles = {ocean.obstacles_number}'))

    @staticmethod
    def print_border(ocean):
        print()
        print('⁕\t' * ocean.num_cols, '⁕\t')
        print()
