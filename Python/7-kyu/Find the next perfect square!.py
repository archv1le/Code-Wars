def find_next_square(sq):
    sqrt_val = int(sq ** 0.5)
    if sqrt_val ** 2 != sq:
        return -1

    next_square = (sqrt_val + 1) ** 2
    return next_square
