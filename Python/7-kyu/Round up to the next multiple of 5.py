def round_to_next5(n):
    next_multiple = (n // 5) * 5
    return next_multiple if next_multiple >= n else next_multiple + 5
