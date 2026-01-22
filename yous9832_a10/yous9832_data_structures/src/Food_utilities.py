"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input('Name: ')
    origin = int(input(f'{Food.origins()}:'))
    vegetarian = input('Vegetarian (Y/N):')
    is_vegetarian = None

    if vegetarian.lower() == 'y':
        is_vegetarian = True
    elif vegetarian.lower() == 'n':
        is_vegetarian = False

    calories = int(input('Calories:'))

    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    items = line.split('|')
    is_vegetarian = None

    if items[2] == 'True':
        is_vegetarian = True
    elif items[2] == 'False':
        is_vegetarian = False

    food = Food(items[0], int(items[1]), is_vegetarian, int(items[3]))

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    foods = []
    line = file_variable.readline().strip()

    while line != '':
        items = line.split('|')
        is_vegetarian = None

        if items[2] == 'True':
            is_vegetarian = True
        elif items[2] == 'False':
            is_vegetarian = False

        food = Food(items[0], int(items[1]),
                    is_vegetarian, int(items[3]))
        foods.append(food)
        line = file_variable.readline().strip()

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for x in foods:
        file_variable.write(
            f'{x.name}|{x.origin}|{x.is_vegetarian}|{x.calories}' + '\n')

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []

    for x in foods:
        if x.is_vegetarian == True:
            veggies.append(x)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    # Your code here

    origins = []

    for x in foods:
        if x.origin == origin:
            origins.append(x)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total = 0

    for x in foods:
        total += x.calories

    avg = int(total/len(foods))

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    o_foods = by_origin(foods, origin)
    avg = int(average_calories(o_foods))

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    lines = ['Food                                Origin       Vegetarian Calories',
             '----------------------------------- ------------ ---------- --------']

    sortedfoods = sorted(foods)

    for x in sortedfoods:
        is_vegetarian = str(x.is_vegetarian)
        origin = Food.ORIGIN[x.origin]
        temp_line = f'{x.name:<36}{origin:<13}{is_vegetarian:>10}{x.calories:>9}'
        lines.append(temp_line)

    for x in lines:
        print(x)

    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    # Your code here

    result = []

    for x in foods:
        if (x.origin == origin or origin == -1) and (x.calories <= max_cals or max_cals == 0) and (x.is_vegetarian == True or is_veg == False):
            result.append(x)

    return result
