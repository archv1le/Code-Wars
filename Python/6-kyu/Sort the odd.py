def sort_array(source_array):
    odd_numbers = [num for num in source_array if num % 2 == 1]

    odd_numbers.sort()

    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd_numbers.pop(0)

    return source_array
