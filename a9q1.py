from copy import deepcopy

# create constants

# list for fruits abbreviation
LIST_OF_FRUITS = ['F', 'W', 'G', 'J', 'M']
# list of fruits full names and their indexes
# in the list of abbreviation to match order in sample output
TREES_DATA = [('Waterfruits', 1), ('Grassfruits', 2), ('Megafriuts', 4), ('Firefruits', 0), ('Joltfruits', 3)]


def create_state(trees_number, trees):
    """
    From list of strings with pairs of coordinates
    for each fruits create trees_number x trees_number square
    with fruits abbreviations in the cells
    with given coordinates and '-' in empty cells.

    :param trees_number: dimension of future garden (int)
    :param trees: list with coordinates for trees (list of strings)
    :return: list of list of strings
    """
    # create trees_number x trees_number matrix
    # where all cells are empty ('-')
    garden = [['-' for i in range(trees_number)] for j in range(trees_number)]
    # for every line in list trees
    for n, line in enumerate(trees):
        # split it by space
        coordinates = line.strip().split()
        # for each coordinate
        # split by coma into two strings
        # convert two strings into integers
        for coordinate in coordinates:
            try:
                i, j = [int(x) for x in coordinate.split(',')]
            # if file format is invalid return empty list
            except ValueError:
                return []
            # try to assign cell with fruit
            try:
                garden[i][j] = LIST_OF_FRUITS[n]
            # if coordinates are out of bounds of matrix
            # return empty list
            except IndexError:
                return []
    return garden


def create_farm(file):
    """
    Read file and create initial garden.

    :param file: name of file to read (str)
    :return: list of list of strings
    """
    # open file
    try:
        with open(file) as f:
            # read first line and convert into integer
            # read other lines
            try:
                trees_number = int(f.readline())
                trees = [line.strip() for line in f.readlines()[:trees_number]]
            # if file has invalid format
            # return empty list
            except (ValueError, IndexError):
                return []
            # create initial state (garden)
            garden = create_state(trees_number, trees)
            return garden
    # if file does not exist
    # return empty list
    except (FileExistsError, FileNotFoundError):
        return []


def trees_around(i, j, garden):
    """
    Return list of adjacent cells
    in matrix for cell with coordinates i and j.

    :param i: number of the row (int)
    :param j: number of the column (int)
    :param garden: matrix to work with (list of lists of strings)
    :return: list of tuples of integers
    """
    list_adjacency = []
    # for all 8 possible adjacent cells
    # check if they are not out of bounds of the matrix
    for x in range(i - 1, i + 2):
        if x not in range(0, len(garden)):
            continue
        for y in range(j - 1, j + 2):
            if y not in range(0, len(garden)):
                continue
            if x == i and y == j:
                continue
            # add valid adjacent coordinates in the list
            list_adjacency.append((x, y))
    return list_adjacency


def get_types(list_adjacency, garden):
    """
    Determine and return types of trees in the cells
    with coordinates from list_adjacency.
    :param list_adjacency: list of tuples of integers
    :param garden: matrix to work with (list of lists of strings)
    :return: list of strings
    """
    tree_list = set()
    # not include abbreviation for megafruit
    # (according to the task it not influence on trees spread) and empty cells
    for (i, j) in list_adjacency:
        if garden[i][j] != '-' and garden[i][j] != 'M':
            tree_list.add(garden[i][j])
    # return unique strings abbreviations of trees from adjacent cells
    return list(tree_list)


def determine_type_tree(trees):
    """
    Determine what type of tree should be grown
    among the list given trees.

    :param trees: trees abbreviations around particular cell (list of strings)
    :return: tree abbreviations to grow (str)
    """
    # adjacent to only one type of tree
    # then that tree type will spread to the space
    if len(trees) == 1:
        return trees[0]
    # adjacent to ALL FOUR types of basic trees
    # then a megafruit tree will grow in that space
    if len(trees) == 4:
        return 'M'
    # adjacent to two or three types of basic trees
    # then the dominant tree type will spread
    if len(trees) == 2 or len(trees) == 3:
        # Joltfruit  dominates  ALL
        if 'J' in trees:
            return 'J'
        if len(trees) == 2:
            # waterfruit  dominates firefruit
            if 'F' in trees and 'W' in trees:
                return 'W'
            # firefruit dominates  grass
            elif 'F' in trees and 'G' in trees:
                return 'F'
            # grassfruit  dominates  water
            elif 'W' in trees and 'G' in trees:
                return 'G'
    # adjacent to exactly three types and none are dominant: then nothing spreads
    return '-'


def spring(garden):
    """
    Simulate one year growth of the garden.

    :param garden: matrix with fruits (list of lists of strings)
    :return: new garden, which no grows anymore (list of lists of strings)
    """
    # copy old garden to build new one
    new_garden = deepcopy(garden)
    # for each cell in the garden
    for i in range(len(garden)):
        for j in range(len(garden)):
            # if cell is empty (there is no tree yet)
            if garden[i][j] == '-':
                # get its adjacent cells
                adjacent_trees = trees_around(i, j, garden)
                trees = get_types(adjacent_trees, garden)
                # determine, which types of fruits current cell is surrounded
                tree = determine_type_tree(trees)
                # assign new tree (or stay empty) to the cell in new garden
                new_garden[i][j] = tree
    return new_garden


def autumn(garden, total_fruits):
    """
    Simulate harvesting in the Fall.

    :param garden: matrix with fruits (list of lists of strings)
    :param total_fruits: list of counts of harvest from previous years (list of int)
    :return: list of int, list of int
    """
    # initiate list with harvest equal to zero
    # to count current year's harvest
    year_harvest = [0, 0, 0, 0, 0]
    # for each cell in garden
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            # if there is fruit in the cell
            if garden[i][j] != '-':
                # determine its abbreviation index from constant LIST_OF_FRUITS
                index = LIST_OF_FRUITS.index(garden[i][j])
                # add 1 to the value with index 'index' in year harvest and total harvest lists
                year_harvest[index] += 1
                total_fruits[index] += 1
    return total_fruits, year_harvest


def grow_garden(garden):
    """
    Simulate growing the garden within all period it can grow.

    :param garden: matrix with fruits (list of lists of strings)
    :return: list of int, list of int, integer
    """
    # initiate list with harvest equal to zero
    # to count all years harvest
    total_fruits = [0, 0, 0, 0, 0]
    # assign years counter to 0
    years = 0
    # while garden is growing
    while True:
        # get new (updated in the spring) state
        spring_garden = spring(garden)
        # count yearly and total harvest
        if years > 0:
            total_fruits, year_harvest = autumn(garden, total_fruits)
        # if garden does not grow anymore
        # return lists with harvests and years counter
        if garden == spring_garden and years > 0:
            return total_fruits, year_harvest, years
        # in other go to next year
        years += 1
        # update garden (state)
        garden = spring_garden


def main():
    """
    Main function.

    :return: NoneType
    """
    # ask user for filename
    file = input('Enter file name: ')
    # initial garden
    garden = create_farm(file)
    # if file was not valid (not exists or data in wrong format)
    # exit
    if not garden:
        return
    # grow garden, count harvest
    total_fruits, last_year_harvest, years = grow_garden(garden)
    # print summary
    print('Fruits yield from final year:')
    print('****************************')
    for (tree, i) in TREES_DATA:
        print('{}: {}'.format(tree, last_year_harvest[i]))
    print()
    print('Total farm yield after {} years:'.format(years))
    print('**********************************')
    for (tree, i) in TREES_DATA:
        print('{}: {}'.format(tree, total_fruits[i]))
    print()


if __name__ == '__main__':
    main()
