def binary_array_to_number(arr):
    decimal = 0
    for bit in arr:
        decimal = decimal * 2 + bit
    return decimal
