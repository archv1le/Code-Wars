def tower_builder(n_floors):
    tower = []
    width = n_floors * 2 - 1

    for i in range(1, n_floors + 1):
        spaces = ' ' * ((width - (2 * i - 1)) // 2)
        stars = '*' * (2 * i - 1)
        tower.append(spaces + stars + spaces)

    return tower
