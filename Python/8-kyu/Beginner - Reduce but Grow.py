def grow(arr):
    from functools import reduce
    return reduce(lambda x, y: x * y, arr)
