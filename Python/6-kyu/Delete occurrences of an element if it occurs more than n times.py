def delete_nth(order,max_e):
    result = []
    occurrences = {}

    for num in order:
        count = occurrences.get(num, 0)
        if count < max_e:
            result.append(num)
            occurrences[num] = count + 1

    return result
