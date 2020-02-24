import a9q1


def test_create_farm():
    """
    Test two functions: create_stage_and_create_farm
    :return:
    """
    files = ['not_exists.txt', 'pokefruit_palletfarm.txt']
    valid_stages = [
        [],
        [['F', '-', '-', 'W'],
         ['-', '-', '-', '-'],
         ['-', '-', '-', '-'],
         ['G', '-', '-', 'J']]
    ]
    try:
        for i, file in enumerate(files):
            stage = a9q1.create_farm(file)
            assert stage == valid_stages[i]
    except AssertionError:
        print('Error in function "create_farm":')
        print('Got:')
        print(stage)
        print('Right:')
        print(valid_stages[i])
    else:
        print('Tests for "create_farm" passed')

def test_create_state():
    stage = ['1,1', '2,0', '2,2']
    num = 3
    valid_stage = [['-', '-', '-'],
             ['-', 'F', '-'],
             ['W', '-', 'G']]
    try:
        garden = a9q1.create_state(num, stage)
        assert valid_stage == garden
    except AssertionError:
        print('Error in function "create_state":')
        print('Got:')
        print(garden)
        print('Right:')
        print(valid_stage)


def test_trees_around():
    garden = [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
    garden_2 = [['-', '-'], ['-', '-']]
    try:
        coordinates = a9q1.trees_around(0, 0, garden)
        valid_coordinates = [(0, 1), (1, 0), (1, 1)]
        assert coordinates == valid_coordinates

        coordinates = a9q1.trees_around(1, 2, garden)
        valid_coordinates = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)]
        assert coordinates == valid_coordinates

        coordinates = a9q1.trees_around(0, 0, garden_2)
        valid_coordinates = [(0, 1), (1, 0), (1, 1)]
        assert coordinates == valid_coordinates


    except AssertionError:
        print('Error in function "trees_around":')
        print('Got:')
        print(coordinates)
        print('Right:')
        print(valid_coordinates)
    else:
        print('Tests for "trees_around" passed')


def test_get_types():
    garden = [
        ['F', '-', 'W', 'W'],
        ['G', '-', 'J', '-'],
        ['-', 'W', '-', '-'],
        ['G', '-', 'F', 'J']
    ]
    coordinates = [
        [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)],
        [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)],
        [(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)]
    ]
    valid_trees = [
        ['F', 'G', 'J', 'W'],
        ['F', 'G', 'W'],
        ['F', 'J', 'W'],
        ['G', 'W']
    ]
    try:
        for i, coordinate in enumerate(coordinates):
            list_trees = a9q1.get_types(coordinate, garden)
            assert sorted(list_trees) == valid_trees[i]
    except AssertionError:
        print('Error in function "get_types":')
        print('Got:')
        print(coordinates)
        print('Right:')
        print(valid_trees)
    finally:
        print('Tests for "get_types" passed')

def test_determine_type_tree():
    stages = [
        ['F', 'J', 'W', 'G'],
        ['F', 'W'],
        ['G', 'W'],
        ['J', 'F'],
        ['F', 'G', 'J'],
        ['F', 'G', 'W']
    ]
    valid_state = ['M', 'W', 'G', 'J', 'J', '-']
    try:
        for i, stage in enumerate(stages):
            result = a9q1.determine_type_tree(stages[i])
            assert result == valid_state[i]
    except AssertionError:
        print('Error in function "determine_type_tree":')
        print('Got:')
        print(result)
        print('Right:')
        print(valid_state[i])
    finally:
        print('Tests for "determine_type_tree" passed')

def test_spring():
    garden_1 = [
        ['F', '-', '-', 'W'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['G', '-', '-', 'J']
    ]
    garden_2 = [
        ['F', '-', '-', 'W'],
        ['-', '-', '-', '-'],
        ['-', 'W', '-', '-'],
        ['G', '-', 'F', 'J']
    ]
    garden_3 = [
        ['F', '-', 'W', 'W'],
        ['G', '-', 'J', '-'],
        ['-', 'W', '-', '-'],
        ['G', '-', 'F', 'J']
    ]
    right_gardens = [
        [['F', 'F', 'W', 'W'],
        ['F', 'F', 'W', 'W'],
        ['G', 'G', 'J', 'J'],
        ['G', 'G', 'J', 'J']],

        [['F', 'F', 'W', 'W'],
        ['W', 'W', 'W', 'W'],
        ['G', 'W', 'J', 'J'],
        ['G', '-', 'F', 'J']],

        [['F', 'M', 'W', 'W'],
        ['G', 'M', 'J', 'J'],
        ['G', 'W', 'J', 'J'],
        ['G', '-', 'F', 'J']],
    ]
    gardens = [garden_1, garden_2, garden_3]
    try:
        for i, garden in enumerate(gardens):
            result = a9q1.spring(garden)
            assert result == right_gardens[i]
    except AssertionError:
        print('Error in function "spring":')
        print('Got:')
        print(result)
        print('Right:')
        print(right_gardens[i])
    finally:
        print('Tests for "spring" passed')


def test_autumn():
    garden_1 = [
        ['F', 'F', 'W', 'W'],
         ['F', 'F', 'W', 'W'],
         ['G', 'G', 'J', 'J'],
         ['G', 'G', 'J', 'J']
    ]
    garden_2 = [
        ['F', 'F', 'W', 'W'],
        ['W', 'W', 'W', 'W'],
        ['G', 'W', 'J', 'J'],
        ['G', '-', 'F', 'J']
    ]
    garden_3 = [
        ['F', 'M', 'W', 'W'],
        ['G', 'M', 'J', 'J'],
        ['G', 'W', 'J', 'J'],
        ['G', 'M', 'F', 'J']
    ]
    total = [[0, 0, 0, 0, 0], [3, 1, 0, 4, 0], [2, 3, 1, 1, 1]]
    right_totals = [[4, 4, 4, 4, 0], [6, 8, 2, 7, 0], [4, 6, 4, 6, 4]]
    right_last = [[4, 4, 4, 4, 0], [3, 7, 2, 3, 0], [2, 3, 3, 5, 3]]
    gardens = [garden_1, garden_2, garden_3]
    try:
        for i, garden in enumerate(gardens):
            result = a9q1.autumn(garden, total[i])
            assert result == (right_totals[i], right_last[i])
    except AssertionError:
        print('Error in function "autumn":')
        print('Got:')
        print(result)
        print('Right:')
        print((right_totals[i], right_last[i]))
    finally:
        print('Tests for "autumn" passed')

def test_grow_garden():
    garden_1 = [
        ['F', '-', '-', 'W'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['G', '-', '-', 'J']
    ]
    garden_2 = [
        ['F', '-', '-', 'W'],
        ['-', '-', '-', '-'],
        ['-', 'W', '-', '-'],
        ['G', '-', 'F', 'J']
    ]
    garden_3 = [
        ['F', '-', 'W', 'W'],
        ['G', '-', 'J', '-'],
        ['-', 'W', '-', '-'],
        ['G', '-', 'F', 'J']
    ]
    garden_4 = [['F', '-', '-', '-'],
                ['G', '-', '-', '-'],
                ['-', 'W', '-', '-'],
                ['G', '-', 'F', 'J']]
    gardens = [garden_1, garden_2, garden_3, garden_4]
    right_answers = [
        ([4, 4, 4, 4, 0], [4, 4, 4, 4, 0], 1), ([6, 14, 4, 6, 1], [3, 7, 2, 3, 1], 2),
        ([4, 6, 6, 10, 5], [2, 3, 3, 5, 3], 2), ([6, 6, 6, 7, 2], [3, 4, 3, 4, 2], 2)
    ]
    try:
        for i, garden in enumerate(gardens):
            answer = a9q1.grow_garden(garden)
            assert right_answers[i] == answer

    except AssertionError:
        print('Error in function "grow_garden":')
        print('Got:')
        print(answer)
        print('Right:')
        print(right_answers[i])
    finally:
        print('Tests for "grow_garden" passed')


def test_all():
    for func in [test_create_farm, test_trees_around, test_get_types, test_grow_garden, test_determine_type_tree, test_spring, test_autumn]:
        func()


test_all()
