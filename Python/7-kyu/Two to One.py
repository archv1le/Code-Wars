def longest(a1, a2):
    combined_set = set(a1 + a2)
    sorted_result = ''.join(sorted(combined_set))
    return sorted_result
