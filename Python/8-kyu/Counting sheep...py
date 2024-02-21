def count_sheeps(sheep):
    if sheep is None:
        return 0

    return sum(1 for s in sheep if s)
