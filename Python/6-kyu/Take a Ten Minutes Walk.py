def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    direction_count = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for direction in walk:
        direction_count[direction] += 1

    if direction_count['n'] != direction_count['s'] or direction_count['e'] != direction_count['w']:
        return False

    return True
